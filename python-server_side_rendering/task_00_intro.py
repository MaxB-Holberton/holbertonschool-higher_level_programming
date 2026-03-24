from os.path import exists

def generate_invitations(template, attendees_list):
    """
        Generate the template
    """

    if not template:
        print("ERROR: missing template file")
        return

    if not attendees_list:
        print("ERROR: missing attendees_list")
        return

    if not isinstance(template, str):
        print("ERROR: template must be a string")
        return

    if not isinstance(attendees_list, list):
        print("ERROR: attendees_list must be a list of dictionaries")
        return

    if not all(isinstance(item, dict) for item in attendees_list):
        print("ERROR: attendees_list must be a list of dictionaries")
        return

    for index, invite in enumerate(attendees_list, start=1):
        invite_content = template
        for key, value in invite.items():
            replacement_values = "{"+f"{key}"+"}"
            new_val = value or "N/A"
            invite_content = invite_content.replace(replacement_values, new_val)
        if not exists(f"output_{index}.txt"):
            with open(f"output_{index}.txt", "w") as file:
                file.write(invite_content)
        else:
            print("ERROR: file already exists")

