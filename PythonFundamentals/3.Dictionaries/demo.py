phonebook = {}
phonebook["John Smith"] = "+1-555-8976"
phonebook["Lisa Smith"] = "+1-555-1234"
phonebook["Sam Doe"] = "+1-555-5030"
phonebook["Nakov"] = "+359-899-555-592"
phonebook["Nakov"] = "+359-2-981-9819"
phonebook.pop("John Smith", None)
if 'Nakov' in phonebook.keys():
    print('Nakov Found!')
else:
    print('Nakov NOT Found')