from browser import document


def check_selection(event):
    select = document['select_id']  # replace "select_id" with the actual id of your select
    button = document["submit"]

    if select.value == "":
        button.style.display = "none"
        if "is-warning" not in select.classList:
            select.classList.add("is-warning")
    else:
        button.style.display = "block"
        select.classList.remove("is-warning")


# attach the function to the change event of the select
document['select_id'].bind('change', check_selection)
