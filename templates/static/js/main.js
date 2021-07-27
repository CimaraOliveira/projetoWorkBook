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

$(document).ready(async function () {
	// essa url retorna a lista dos usuarios?e
	//const data = await Req.getJSON("http://127.0.0.1:8000/api/usuario/", null)
	//console.log(await data.json())
	if ($("#list-mensagens").length) {
		const data = await Req.getJSON(`${uri_by_last_messages}`, { id: 1 })
		createList(await data.json())
		//const d = await Req.getJSON(`${uri_by_last_messages}`, {id: 1})
		//console.log(await d.json())
		//createListMensagens();
		// para mostrar as mensagens na div bate-papo. vc precisa cria um recurso (APi) para retornar essas mensagens. vc pode usar as consultas que tem na parte web
	}
});

function createListMensagens() {
	function getDestinatario() {
		const spanName = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-name pull-left' }, value: 'Teste' })
		const spanData = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-timestamp pull-right' }, value: '20/07/2021' })
		const divDirectInfo = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-info clearfix' }, children: [spanName, spanData] })
		const image = new Tag({ tagName: 'img', attrs: { src: 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png', class: 'direct-chat-img' } })
		const divDirectText = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-text' }, value: 'Olá Mundo!' })
		const divDirectDestinatario = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-msg' }, children: [divDirectInfo, image, divDirectText] })
		return divDirectDestinatario
	}

	function getRemetente() {
		const spanName = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-name pull-left' }, value: 'Teste' })
		const spanData = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-timestamp pull-right' }, value: '20/07/2021' })
		const divDirectInfo = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-info clearfix' }, children: [spanName, spanData] })
		const image = new Tag({ tagName: 'img', attrs: { src: 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png', class: 'direct-chat-img' } })
		const divDirectText = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-text' }, value: 'Olá Mundo!' })
		const divDirectRemetente = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-msg right' }, children: [divDirectInfo, image, divDirectText] })
		return divDirectRemetente
	} 
	View.append(new TagView(getDestinatario()).element, document.getElementById('direct-chat'));
	View.append(new TagView(getRemetente()).element, document.getElementById('direct-chat'));
}

async function createList(data) { 
	const idUser = 1
	for (let obj of data) {
		const resDes = await Req.getJSON(`${baseURI}/api/usuario/`, [obj['destinatario']])
		obj['destinatario'] = await resDes.json()
		const resReme = await Req.getJSON(`${baseURI}/api/usuario/`, [obj['remetente']])
		obj['remetente'] = await resReme.json()
		if (obj['remetente'].id === idUser){
			getRemetente(obj)
			console.log('rem')
		}  else {
			console.log('des')
			getDestinatario(obj)
		}	
	}

	function getRemetente(obj) {
		const img = new Tag({ tagName: 'img', attrs: { src: obj['remetente'].imagem !== null ? obj['remetente'].imagem : 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png', style: 'max-width: 500px; height: auto' } })
		const divImg = new Tag({ tagName: 'div', attrs: { class: 'product-img' }, children: [img] })
		const pUsername = new Tag({ tagName: 'p', value: obj['remetente'].username, attrs: { class: 'text-black-50' } })
		const spanDataMensagem = new Tag({ tagName: 'span', attrs: { class: 'label label-primary pull-right' }, value: obj.data_mensagem })
		const spanTexto = new Tag({ tagName: 'span', attrs: { class: 'product-description' }, value: obj.texto })
		const divInfo = new Tag({ tagName: 'div', attrs: { class: 'product-info' }, children: [pUsername, spanDataMensagem, spanTexto] })
		const a = new Tag({ tagName: 'a', attrs: { class: 'product-title' }, children: [divImg, divInfo] })
		const li = new Tag({ tagName: 'li', attrs: { class: 'item' }, children: [a] })
		const liView = new TagView(li)
		View.append(liView.element, document.getElementById('list-mensagens'))
	}

	function getDestinatario(obj) {
		const img = new Tag({ tagName: 'img', attrs: { src: obj['destinatario'].imagem !== null ? obj['destinatario'].imagem : 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png', style: 'max-width: 500px; height: auto' } })
		const divImg = new Tag({ tagName: 'div', attrs: { class: 'product-img' }, children: [img] })
		const pUsername = new Tag({ tagName: 'p', value: obj['destinatario'].username, attrs: { class: 'text-black-50' } })
		const spanDataMensagem = new Tag({ tagName: 'span', attrs: { class: 'label label-primary pull-right' }, value: obj.data_mensagem })
		const spanTexto = new Tag({ tagName: 'span', attrs: { class: 'product-description' }, value: obj.texto })
		const divInfo = new Tag({ tagName: 'div', attrs: { class: 'product-info' }, children: [pUsername, spanDataMensagem, spanTexto] })
		const a = new Tag({ tagName: 'a', attrs: { class: 'product-title' }, children: [divImg, divInfo] })
		const li = new Tag({ tagName: 'li', attrs: { class: 'item' }, children: [a] })
		const liView = new TagView(li)
		View.append(liView.element, document.getElementById('list-mensagens'))
	}
}