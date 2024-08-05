from browser import document


def validate_textarea(event):
    textarea = event.target
    text = textarea.value
    min_length = int(textarea.get('data-minlength', '0'))
    max_length = int(textarea.get('data-maxlength', '0'))

    error_message = document.select('.help.is-danger', within=textarea.parent)[0]

    if min_length and len(text) < min_length:
        textarea.classList.add('is-danger')
        error_message.text = 'Text should be at least {} characters.'.format(min_length)
        error_message.style.display = 'block'
    elif max_length and len(text) > max_length:
        textarea.classList.add('is-danger')
        error_message.text = 'Text should be at most {} characters.'.format(max_length)
        error_message.style.display = 'block'
    else:
        textarea.classList.remove('is-danger')
        error_message.style.display = 'none'


# Attach the function to the 'input' event of the textarea
document['textarea_id'].bind('input', validate_textarea)  # replace 'textarea_id' with the actual id of your textarea
