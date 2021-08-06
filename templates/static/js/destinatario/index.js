function getDestinatarioBatePapo(dest, mensagem) {
	console.log('dest',dest)
	const spanName = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-name pull-left' }, value: dest.username })
	const spanData = new Tag({ tagName: 'span', attrs: { class: 'direct-chat-timestamp pull-right' }, value: mensagem.data_mensagem})
	const divDirectInfo = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-info clearfix' }, children: [spanName, spanData] })
	const image = new Tag({ tagName: 'img', attrs: { src: dest.imagem, 
	class: 'direct-chat-img' } })
	const divDirectText = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-text' }, value: mensagem.texto })
	const divDirectDestinatario = new Tag({ tagName: 'div', attrs: { class: 'direct-chat-msg' }, children: [divDirectInfo, image, divDirectText] })
	View.append(new TagView(divDirectDestinatario).element, document.getElementById('direct-chat'));
}

function getDestinatarioList(dest, rem, messagem) { 
    const img = new Tag({ tagName: 'img', attrs: { src: dest.imagem !== null ? dest.imagem : 'https://i.pinimg.com/originals/0c/3b/3a/0c3b3adb1a7530892e55ef36d3be6cb8.png', style: 'max-width: 500px; height: auto' } })
    const divImg = new Tag({ tagName: 'div', attrs: { class: 'product-img' }, children: [img] })
    const pUsername = new Tag({ tagName: 'p', value: dest.username, attrs: { class: 'text-black-50' } })
    const spanDataMensagem = new Tag({ tagName: 'span', attrs: { class: 'label label-primary pull-right' }, value: messagem.data_mensagem })
    const spanTexto = new Tag({ tagName: 'span', attrs: { class: 'product-description' }, value: messagem.texto })
    const divInfo = new Tag({ tagName: 'div', attrs: { class: 'product-info' }, children: [pUsername, spanDataMensagem, spanTexto] })
    const a = new Tag({ tagName: 'a', attrs: { class: 'product-title', href: '#'}, children: [divImg, divInfo] })
    const li = new Tag({ tagName: 'li', attrs: { class: 'item' }, children: [a] })
    const liView = new TagView(li)
    liView.element.addEventListener('click', async () => await batePapo(rem, dest.id), false);
    View.append(liView.element, document.getElementById('list-mensagens'))
}