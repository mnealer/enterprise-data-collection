from browser import document


def validate_element(event):
    field = event.target
    value = field.value
    validation_rules = field.attrs.get('data-validation', '').split(',')
    valid = True
    message = ''

    for rule in validation_rules:
        if ':' in rule:
            rule_name, rule_val = rule.split(':')
            if rule_name == 'minlength' and len(value) < int(rule_val):
                valid = False
                message = 'Minimum length is {} characters.'.format(rule_val)
                break
        elif rule == 'required' and not value:
            valid = False
            message = 'This field is required.'
            break

    error_message = document.select('.help.is-danger', within=field.parent)[0]

    if valid:
        field.classList.remove('is-danger')
        error_message.style.display = 'none'
    else:
        field.classList.add('is-danger')
        error_message.text = message
        error_message.style.display = 'block'


# Attach the function to the 'input' event of the text input
document['text_input'].bind('input', validate_element)
