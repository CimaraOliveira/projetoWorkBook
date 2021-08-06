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
const uri_by_last_messages = `${baseURI}/api/mensagem/get_by_last_messages`;
const uri_by_messages = `${baseURI}/api/mensagem/get_by_detalhe_mensagens/`;
const uri_post_messages = `${baseURI}/api/mensagem/`;
const uri_api_token = `${baseURI}/api-token/`
const uri_api_auth_key = `${baseURI}/api/usuario/get_by_auth_key/`
const uri_api_username_password = `${baseURI}/api/usuario/get_by_username_password/`
let idUser = -1
let key = null
let basic = null
const keyIdPerfil = 'id-perfil'

function get_csrftoken(){
	const coo = document.cookie
	const index = coo.search('csrftoken')
	if (index > -1){
		return coo.substring(coo.search('=') + 1, document.cookie.length)
	}
	return ""
}

function save_id_perfil(){
	Session.create('id-perfil', document.getElementById('id-perfil').textContent)
	window.location.href = "/mensagem/teste-chat/"//aqui. show kkkkk. pois vlw, vou sair
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
		await render()// ta. outra coisa, ficou com alguma duvida dessa funcionalidade. show. depois vc muda a url pra ficar mais legal, lembre de alterar na funcao que ela ta direcionando para a tela de teste
	}
});

async function render(){
	document.getElementById('list-mensagens').innerHTML = ""
	await Req.getJSON({uri: `${uri_by_last_messages}`, headers:{
		'Authorization': basic
	}, params: { token: key.key },
	onSuccess: async (data) => await createList(data), onError: (data) => console.log(data)})
}

async function batePapo(remetente, destinatario){
	await Req.getJSON({uri: `${uri_by_messages}`, params: {remetente: remetente, destinatario: destinatario}
	, onSuccess: async (res) => await mensagens(res), onError: () => {}})

	async function mensagens(res){
		const {data} = res 
		document.getElementById('direct-chat').innerHTML = ""
		document.getElementById('direct-chat-footer').innerHTML = ""
		for (let obj of data){
			await createListMensagensBatePapo(obj)
		}
		if (remetente === idUser){
			footer(destinatario, remetente)
		} else {
			footer(remetente, destinatario)
		}
	}
	
}
 
function footer(destinatario, remetente){
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
	buttonElement.addEventListener('click', async () => await enviarMensagem(value, destinatario, remetente, inputElement), false)
	View.append(element, document.getElementById('direct-chat-footer'));
}

async function enviarMensagem(value, destinatario, remetente, input){ 
	if (value !== ''){
		await Req.postJSON({uri: `${uri_post_messages}`, body: {
			texto: value,
			destinatario: destinatario,
			remetente: remetente,
			data_mensagem: new Date()
		}, headers: {
			'Authorization': `Basic ${basic}`,
			'X-CSRFToken': get_csrftoken()
		}, onSuccess: async (res) => await createListMensagensBatePapo(res.data, true), onError: (data) => console.log(data)})
		value = ""
		input.value = value
	}
} 

async function createListMensagensBatePapo(mensagem, isRefresh) {
	
	if (idUser === mensagem.remetente){ 
		const resp = await Req.getJSON({uri: `${baseURI}/api/usuario/`,
		params: [mensagem.remetente], 
		})
		if (resp.status === 200){
			const body = await resp.json()
			getRemetenteBatePapo(body, mensagem) 
		}
	} else { 
		const resp = await Req.getJSON({uri: `${baseURI}/api/usuario/`, params: [mensagem.remetente], 
		})
		if (resp.status === 200){
			const body = await resp.json()
			getDestinatarioBatePapo(body, mensagem)
		}
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

async function createList(res) { 
	const {data} = res
	
	for (let obj of data) {
		if (idUser !== obj['remetente']){
			const resp = await Req.getJSON({uri: `${baseURI}/api/usuario/`,
			params: [obj['remetente']]})
			if (resp.status === 200){
				const body = await resp.json()
				getRemetenteList(body, obj['destinatario'], obj)
			}
		} else {
			const resp = await Req.getJSON({uri: `${baseURI}/api/usuario/`, params: [obj['destinatario']]})
			if (resp.status === 200){
				const body = await resp.json()
				getDestinatarioList(body, obj['remetente'], obj)
			}
		}  
	} 
	
}