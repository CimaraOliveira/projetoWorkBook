function save_id_perfil(id, notificacao) {
	if ($("#id-perfil").length && typeof id === 'undefined' && typeof notificacao === 'undefined') { // essa verificacao vai tratar se existe o id do usuario e da notificacao
		Session.create(keyIdPerfil, document.getElementById(keyIdPerfil).textContent)
	} else if (typeof id !== 'undefined' && typeof notificacao !== 'undefined') {// se existe ele vai salvar na memoria do navegador
		Session.create(keyIdPerfil, id)
		Session.create(keyIdNotificacao, [notificacao])
	}
	window.location.href = "/mensagem/teste-chat/"
}

async function enviar_mensagem_pelo_perfil(id) { 
	if (id !== null) {
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

async function render() {
	document.getElementById('list-mensagens').innerHTML = ""
	await Req.getJSON({
		uri: `${uri_by_last_messages}`, headers: {
			'Authorization': basic
		}, params: { token: key.key },
		onSuccess: async (data) => await createList(data), onError: (data) => console.error(data)
	})
}

function scroll(){
    const direct = document.getElementById('direct-chat')
    direct.scrollTop = direct.scrollHeight
}

async function batePapo(remetente, destinatario) {
    let notificacoes = JSON.parse(Session.get(keyIdNotificacao))
    if (notificacoes === null){
        notificacoes = await getByRemetenteAndDestinatario(remetente, destinatario)
    }

	await Req.getJSON({
		uri: `${uri_by_messages_detalhe}`, params: { remetente: remetente, destinatario: destinatario }
		, onSuccess: async (res) => await mensagens(res), onError: () => { }
	})

	async function mensagens(res) {
		const { data } = res
        const direct = document.getElementById('direct-chat')
		direct.innerHTML = ""
		document.getElementById('direct-chat-footer').innerHTML = ""
		
		for (let obj of data) {
			await createListMensagensBatePapo(obj)
		}
		if (notificacoes !== null) {
            console.log(notificacoes)
			if (Array.isArray(notificacoes)){
                for (let notificacao of notificacoes){
                    await Req.putJSON({
                        uri: `${uri_api_notificacao_set_status}`, body: {}, params: { id: notificacao.id }, headers: {
                            'Authorization': `Basic ${basic}`,
                            'X-CSRFToken': get_csrftoken()
                        }, onSuccess: ()=> {
                            Session.remove(keyIdNotificacao)
                            atualizarNotificacoes()
                        }, onError: ()=>{}
                    })
                }
            }
		}
		if (remetente === idUser) {
			footer(destinatario, remetente)
		} else {
			footer(remetente, destinatario)
		}
        scroll()
	}

}

function footer(destinatario, remetente) {
	let value = ""
	const input = new Tag({ tagName: 'input', attrs: { type: 'text', name: 'texto', placeholder: 'Digite uma mensagem', class: 'form-control' } })
	const i = new Tag({ tagName: 'i', attrs: { class: 'fa fa-paper-plane' } })
	const button = new Tag({
		tagName: 'button', attrs: { type: 'button', class: 'btn btn-primary block' },
		children: [i]
	})
	const span = new Tag({ tagName: 'span', attrs: { class: 'input-group-btn' }, children: [button] })
	const divInputGroup = new Tag({ tagName: 'div', attrs: { class: 'input-group' }, children: [input, span] })
	const element = new TagView(divInputGroup).element;
	const buttonElement = element.getElementsByTagName('button').item(0)
	const inputElement = element.getElementsByTagName('input').item(0)
	inputElement.addEventListener('keyup', (event) => {
		value = event.target.value
	}, false)
	buttonElement.addEventListener('click', async () => await enviarMensagem(value, destinatario, remetente, inputElement), false)
	View.append(element, document.getElementById('direct-chat-footer'));
}

async function enviarMensagem(value, destinatario, remetente, input) {
	if (value !== '') {
		await Req.postJSON({
			uri: `${uri_api_messages}`, body: {
				texto: value,
				destinatario: destinatario,
				remetente: remetente,
				data_mensagem: new Date()
			}, headers: {
				'Authorization': `Basic ${basic}`,
				'X-CSRFToken': get_csrftoken()
			}, onSuccess: async (res) => await createListMensagensBatePapo(res.data, true), onError: (data) => console.log(data)
		})
		value = ""
		input.value = value
	}
}

async function createListMensagensBatePapo(mensagem, isRefresh) {
	if (idUser === mensagem.remetente) {
		getRemetenteBatePapo(await getUser(mensagem.remetente), mensagem)
	} else {
		getDestinatarioBatePapo(await getUser(mensagem.remetente), mensagem)
	}
	if (isRefresh) {
		await render()
	}
    
    scroll()
}

/*function await render(){
	setInterval(async () =>{
	  await render()
	}, 1000)
}*/

async function createList(res) {
	const { data } = res
	console.log('data -> ', data)
	for (let obj of data) {
		if (idUser !== obj['remetente']) {
			getRemetenteList(await getUser(obj['remetente']), obj['destinatario'], obj)
		} else {
			getDestinatarioList(await getUser(obj['destinatario']), obj['remetente'], obj)
		}
	}

}