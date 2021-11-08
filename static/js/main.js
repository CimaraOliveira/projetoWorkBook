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
const baseURI = "https://workbook-teste.herokuapp.com";
const uri_api_notificacao = `${baseURI}/api/notificacao/`
const uri_api_messages = `${baseURI}/api/mensagem/`;
const uri_api_token = `${baseURI}/api-token/`
const uri_api_usuario = `${baseURI}/api/usuario/`
const uri_api_auth_key = `${uri_api_usuario}get_by_auth_key/`
//----------------------------------
const uri_api_username_password = `${uri_api_usuario}get_by_username_password/`
const uri_by_messages_detalhe = `${uri_api_messages}get_by_detalhe_mensagens/`
const uri_by_last_messages = `${uri_api_messages}get_by_last_messages`
const uri_api_notificacao_get_by_remetente_and_destinatario = `${uri_api_notificacao}get_by_remetente_and_destinatario/`
const uri_api_notificacao_get_status = `${uri_api_notificacao}get_status`
const uri_api_notificacao_set_status = `${uri_api_notificacao}atualizar_status/`
let idUser = -1
let key = null
let basic = null
const keyIdPerfil = 'id-perfil'
const keyIdNotificacao = "id-notificacao"

function get_csrftoken() {
	const coo = document.cookie
	const index = coo.search('csrftoken')
	if (index > -1) {
		return coo.substring(coo.search('=') + 1, document.cookie.length)
	}
	return ""
}

async function getUser(id) {
	const resp = await Req.getJSON({
		uri: `${uri_api_usuario}get_by_id/`,
		params: { id: id },
	})
	if (resp.status === 200) {
		return await resp.json()
	}
	return null
}