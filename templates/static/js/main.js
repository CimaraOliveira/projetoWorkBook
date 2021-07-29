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
const idUser = 1

$(document).ready(async function () {
	// essa url retorna a lista dos usuarios?e
	//const data = await Req.getJSON("http://127.0.0.1:8000/api/usuario/", null)
	//console.log(await data.json())
	if ($("#list-mensagens").length) {
		await Req.getJSON({uri: `${uri_by_last_messages}`, params: { id: 1 },
		onSuccess: (data) => createList(data), onError: (data) => console.log(data)})
		//const d = await Req.getJSON(`${uri_by_last_messages}`, {id: 1})
		//console.log(await d.json())
		//createListMensagens();
		// para mostrar as mensagens na div bate-papo. vc precisa cria um recurso (APi) para retornar essas mensagens. vc pode usar as consultas que tem na parte web
	}
});

function batePapo(remetente, destinatario){
	Req.getJSON({uri: `${uri_by_messages}`, params: {remetente: remetente, destinatario: destinatario}
	, onSuccess: (res) => mensagens(res), onError: () => {}})

	function mensagens(res){
		const {data} = res 
		document.getElementById('direct-chat').innerHTML = ""
		document.getElementById('direct-chat-footer').innerHTML = ""
		for (let obj of data){
			createListMensagens(obj)
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
	buttonElement.addEventListener('click', () => enviarMensagem(value, destinatario, remetente, inputElement), false)
	View.append(element, document.getElementById('direct-chat-footer'));
}

function enviarMensagem(value, destinatario, remetente, input){
	if (value !== ''){
		/*Req.postJSON({uri: `${uri_post_messages}`, body: {
			texto: value,
			destinatario: destinatario,
			remetente: remetente
		}, headers: {
			'Authorization': `Token e01d52b65cb5a82212d473558bfd57de62a2ecc1`
		}, onSuccess: (res) => createListMensagens(res.data), onError: (data) => console.log(data)})
		value = ""
		input.value = value*/
		console.log(destinatario, remetente, idUser)
	}
}

function createListMensagens(mensagem) {
	
	if (idUser === mensagem.remetente){
		console.log('r', mensagem.remetente)
		Req.getJSON({uri: `${baseURI}/api/usuario/`,
		params: [mensagem.remetente], onSuccess: (res) => getRemetenteBatePapo(res.data, mensagem), onError: (data) => console.log(data)})
	} else {
		console.log( 'd', mensagem.destinatario)
		Req.getJSON({uri: `${baseURI}/api/usuario/`, params: [mensagem.remetente],
		onSuccess: (res) => getDestinatarioBatePapo(res.data, mensagem), onError: (data) => console.log(data)})
	}

	function getDestinatarioBatePapo(dest, mensagem) {
		console.log(dest)
		const spanName = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-name pull-left' }, value: dest.username })
		const spanData = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-timestamp pull-right' }, value: mensagem.data_mensagem})
		const divDirectInfo = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-info clearfix' }, children: [spanName, spanData] })
		const image = new Tag({ tagName: 'img', attrs: { src: dest.imagem, 
		class: 'direct-chat-img' } })
		const divDirectText = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-text' }, value: mensagem.texto })
		const divDirectDestinatario = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-msg' }, children: [divDirectInfo, image, divDirectText] })
		View.append(new TagView(divDirectDestinatario).element, document.getElementById('direct-chat'));
	}

	function getRemetenteBatePapo(rem, mensagem) {
		console.log(rem)
		const spanName = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-name pull-left' }, value: rem.username })
		const spanData = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-timestamp pull-right' }, value: mensagem.data_mensagem })
		const divDirectInfo = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-info clearfix' }, children: [spanName, spanData] })
		const image = new Tag({ tagName: 'img', attrs: { src: rem.imagem, class: 'direct-chat-img' } })
		const divDirectText = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-text' }, value: mensagem.texto })
		const divDirectRemetente = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-msg right' }, children: [divDirectInfo, image, divDirectText] })
		View.append(new TagView(divDirectRemetente).element, document.getElementById('direct-chat'));
	}  
	
}

async function createList(res) { 
	const {data} = res
	
	for (let obj of data) {
		if (idUser === obj['remetente']){
			Req.getJSON({uri: `${baseURI}/api/usuario/`,
			params: [obj['remetente']], onSuccess: (res) => getRemetente(res.data, obj['destinatario'], obj), onError: (data) => console.log(data)})
		} else {
			Req.getJSON({uri: `${baseURI}/api/usuario/`, params: [obj['destinatario']],
			onSuccess: (res) => getDestinatario(res.data, obj['remetente'], obj), onError: (data) => console.log(data)})
		}  
	}

	function getRemetente(rem, dest, mensagem) {   
		const img = new Tag({ tagName: 'img', attrs: { src: rem.imagem !== null ? rem.imagem : 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png', style: 'max-width: 500px; height: auto' } })
		const divImg = new Tag({ tagName: 'div', attrs: { class: 'product-img' }, children: [img] })
		const pUsername = new Tag({ tagName: 'p', value: rem.username, attrs: { class: 'text-black-50' } })
		const spanDataMensagem = new Tag({ tagName: 'span', attrs: { class: 'label label-primary pull-right' }, value: mensagem.data_mensagem })
		const spanTexto = new Tag({ tagName: 'span', attrs: { class: 'product-description' }, value: mensagem.texto })
		const divInfo = new Tag({ tagName: 'div', attrs: { class: 'product-info' }, children: [pUsername, spanDataMensagem, spanTexto] })
		const a = new Tag({ tagName: 'a', attrs: { class: 'product-title', href: '#'}, children: [divImg, divInfo] })
		const li = new Tag({ tagName: 'li', attrs: { class: 'item' }, children: [a] })
		const liView = new TagView(li)
		liView.element.addEventListener('click', () => batePapo(rem.id, dest), false);
		View.append(liView.element, document.getElementById('list-mensagens'))
	}

	function getDestinatario(dest, rem, messagem) { 
		const img = new Tag({ tagName: 'img', attrs: { src: dest.imagem !== null ? dest.imagem : 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png', style: 'max-width: 500px; height: auto' } })
		const divImg = new Tag({ tagName: 'div', attrs: { class: 'product-img' }, children: [img] })
		const pUsername = new Tag({ tagName: 'p', value: dest.username, attrs: { class: 'text-black-50' } })
		const spanDataMensagem = new Tag({ tagName: 'span', attrs: { class: 'label label-primary pull-right' }, value: messagem.data_mensagem })
		const spanTexto = new Tag({ tagName: 'span', attrs: { class: 'product-description' }, value: messagem.texto })
		const divInfo = new Tag({ tagName: 'div', attrs: { class: 'product-info' }, children: [pUsername, spanDataMensagem, spanTexto] })
		const a = new Tag({ tagName: 'a', attrs: { class: 'product-title', href: '#'}, children: [divImg, divInfo] })
		const li = new Tag({ tagName: 'li', attrs: { class: 'item' }, children: [a] })
		const liView = new TagView(li)
		liView.element.addEventListener('click', () => batePapo(rem, dest.id), false);
		View.append(liView.element, document.getElementById('list-mensagens'))
	}
}