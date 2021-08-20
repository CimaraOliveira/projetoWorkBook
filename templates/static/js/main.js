(function () {
	"use strict";

	var treeviewMenu = $('.app-menu');

	// Toggle Sidebar
	$('[data-toggle="sidebar"]').click(function (event) {
		event.preventDefault();
		$('.app').toggleClass('sidenav-toggled');
	});

	// Activate sidebar treeview toggle
	$("[data-toggle='treeview']").click(function (event) {
		event.preventDefault();
		if (!$(this).parent().hasClass('is-expanded')) {
			treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
		}
		$(this).parent().toggleClass('is-expanded');
	});

	// Set initial active toggle
	$("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

	//Activate bootstrip tooltips
	$("[data-toggle='tooltip']").tooltip();

})();
const baseURI = "http://127.0.0.1:8000";
const uri_api_notificacao = `${baseURI}/api/notificacao/`
const uri_api_messages = `${baseURI}/api/mensagem/`;
const uri_api_token = `${baseURI}/api-token/`
const uri_api_usuario = `${baseURI}/api/usuario/`
const uri_api_auth_key = `${uri_api_usuario}get_by_auth_key/`
//----------------------------------
const uri_api_username_password = `${uri_api_usuario}get_by_username_password/`
const uri_by_messages_detalhe = `${uri_api_messages}get_by_detalhe_mensagens/`;
const uri_by_last_messages = `${uri_api_messages}get_by_last_messages`;
const uri_api_notificacao_get_status = `${uri_api_notificacao}get_status`
const uri_api_notificacao_set_status = `${uri_api_notificacao}atualizar_status/` 
let idUser = -1
let key = null
let basic = null
const keyIdPerfil = 'id-perfil'
const keyIdNotificacao = "id-notificacao"

function get_csrftoken(){
	const coo = document.cookie
	const index = coo.search('csrftoken')
	if (index > -1){
		return coo.substring(coo.search('=') + 1, document.cookie.length)
	}
	return ""
}

function save_id_perfil(id, idNotificacao){
	if ($("#id-perfil").length && typeof id === 'undefined' && typeof idNotificacao === 'undefined'){ // essa verificacao vai tratar se existe o id do usuario e da notificacao
		Session.create(keyIdPerfil, document.getElementById(keyIdPerfil).textContent)
	} else if (typeof id !== 'undefined' && typeof idNotificacao !== 'undefined'){// se existe ele vai salvar na memoria do navegador
		Session.create(keyIdPerfil, id)
		Session.create(keyIdNotificacao, idNotificacao)
	}
	window.location.href = "/mensagem/teste-chat/"
}

async function enviar_mensagem_pelo_perfil(id){
	//enviar-mensagem-perfil
	//id-perfil
	if (id !== null){
		await batePapo(idUser, id)
		Session.remove(keyIdPerfil)
	}

}

$(document).ready(async function () { 
	if ($("#list-mensagens").length) {
		key = JSON.parse(Session.get('key'))
		basic = JSON.parse(Session.get('basic'))
		let id = JSON.parse(Session.get('id')) 
		idUser = id.id
		const idPerfil = JSON.parse(Session.get(keyIdPerfil))
		await enviar_mensagem_pelo_perfil(idPerfil)
		await render()
	}
});

async function render(){
	document.getElementById('list-mensagens').innerHTML = ""
	await Req.getJSON({uri: `${uri_by_last_messages}`, headers:{
		'Authorization': basic
	}, params: { token: key.key },
	onSuccess: async (data) => await createList(data), onError: (data) => console.error(data)})
}

async function batePapo(remetente, destinatario){
	await Req.getJSON({uri: `${uri_by_messages_detalhe}`, params: {remetente: remetente, destinatario: destinatario}
	, onSuccess: async (res) => await mensagens(res), onError: () => {}})

	async function mensagens(res){
		const {data} = res 
		document.getElementById('direct-chat').innerHTML = ""
		document.getElementById('direct-chat-footer').innerHTML = ""
		const idNotificacao = JSON.parse(Session.get(keyIdNotificacao))
		for (let obj of data){
			await createListMensagensBatePapo(obj)
		}
		if (remetente === idUser){
			footer(destinatario, remetente, idNotificacao)
		} else {
			footer(remetente, destinatario, idNotificacao)
		}
	}
	
}
 
function footer(destinatario, remetente, idNotificacao){
	let value = ""
	const input = new Tag({tagName: 'input', attrs: {type: 'text', name: 'texto', placeholder: 'Digite uma mensagem', class: 'form-control'}})
	const i = new Tag({tagName: 'i', attrs: {class: 'fa fa-paper-plane'}})
	const button = new Tag({tagName: 'button', attrs: {type: 'button', class: 'btn btn-primary block'},
		children: [i]
	})
	const span = new Tag({tagName: 'span', attrs: {class: 'input-group-btn'}, children: [button]})
	const divInputGroup = new Tag({tagName: 'div', attrs: {class: 'input-group'}, children: [input, span]})
	const element = new TagView(divInputGroup).element;
	const buttonElement = element.getElementsByTagName('button').item(0)
	const inputElement = element.getElementsByTagName('input').item(0)
	inputElement.addEventListener('keyup', (event) => {
		value = event.target.value
	}, false)
	buttonElement.addEventListener('click', async () => await enviarMensagem(value, destinatario, remetente, inputElement, idNotificacao), false)
	View.append(element, document.getElementById('direct-chat-footer'));
}

async function enviarMensagem(value, destinatario, remetente, input, idNotificacao){ 
	if (value !== ''){
		await Req.postJSON({uri: `${uri_api_messages}`, body: {
			texto: value,
			destinatario: destinatario,
			remetente: remetente,
			data_mensagem: new Date()
		}, headers: {
			'Authorization': `Basic ${basic}`,
			'X-CSRFToken': get_csrftoken()
		}, onSuccess: async (res) => await createListMensagensBatePapo(res.data, true, idNotificacao), onError: (data) => console.log(data)})
		value = ""
		input.value = value
	}
} 

async function createListMensagensBatePapo(mensagem, isRefresh, idNotificacao) {
	
	if (idUser === mensagem.remetente){  
		getRemetenteBatePapo(await getUser(mensagem.remetente), mensagem)  
	} else {  
		getDestinatarioBatePapo(await getUser(mensagem.remetente), mensagem) 
	}
	//se amanha der certo. vemos isso e se der tempo iniciamos o socket ta. vou sair, lembre de exlucir ta certo
	if (idNotificacao !== null){
		await Req.putJSON({uri: `${uri_api_notificacao_set_status}`, params: {id: idNotificacao}, headers: {
			'Authorization': `Basic ${basic}`,
			'X-CSRFToken': get_csrftoken()
		}})
	}
	if (isRefresh){
		await render()			
	}  
	
}

/*function await render(){
	setInterval(async () =>{
	  await render()
	}, 1000)
}*/

async function getUser(id){
	const resp = await Req.getJSON({uri: `${uri_api_usuario}get_by_id/`,
		params: {id: id}, 
		})
	if (resp.status === 200){
		return await resp.json()
	}	
	return null
}

async function createList(res) { 
	const {data} = res
	for (let obj of data) {
		if (idUser !== obj['remetente']){
			getRemetenteList(await getUser(obj['remetente']), obj['destinatario'], obj)
		} else {
			getDestinatarioList(await getUser(obj['destinatario']), obj['remetente'], obj)
		}  
	} 
	
}