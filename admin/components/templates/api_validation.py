from browser import ajax, document


def validate_input(event):
    input_elem = event.target
    model_name = input_elem.get(
        'data-model-name')  # Assuming model_name is stored as a data attribute on the input element
    field = input_elem.name
    value = input_elem.value

    data = {'model_name': model_name, 'field': field, 'value': value}

    req = ajax.ajax()
    req.bind('complete', lambda _: handle_response(req, input_elem))
    req.open('POST', '/validate', True)
    req.set_header('content-type', 'application/json')
    req.send(data)


def handle_response(req, input_elem):
    if req.status == 200 and req.responseText == 'false':
        input_elem.classList.add('is-danger')
        error_message = document.select('.help.is-danger', within=input_elem.parent)[0]
        error_message.style.display = 'block'
    elif req.responseText == 'true':
        input_elem.classList.remove('is-danger')
        error_message = document.select('.help.is-danger', within=input_elem.parent)[0]
        error_message.style.display = 'none'


# Attach the function to the 'input' event of the text input
for input_elem in document.select('input[data-model-name]'):
    input_elem.bind('input', validate_input)
