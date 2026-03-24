from os.path import exists

def generate_invitations(template, attendees_list):
    """
        Generate the template
    """

    if not template:
        print("ERROR: missing template file")

    if not attendees_list:
        print("ERROR: missing attendees_list")

    if not isinstance(template, str):
        print("ERROR: template must be a string")

    if not isinstance(attendees_list, list):
        print("ERROR: attendees_list must be a list of dictionaries")

    if not all(isinstance(item, dict) for item in attendees_list):
        print("ERROR: attendees_list must be a list of dictionaries")


    for index, invite in enumerate(attendees_list, start=1):
        new_invite = template
        for key, value in invite.items():
            replacement_values = "{"+f"{key}"+"}"
            new_val = value or "N/A"
            new_invite = new_invite.replace(replacement_values, new_val)
            print(f"{key} + {value}")
        if not exists(f"output_{index}.txt"):
            with open(f"output_{index}.txt", "w") as file:
                file.write(new_invite)
        else:
            print("ERROR: file already exists")

