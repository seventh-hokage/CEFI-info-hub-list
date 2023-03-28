import yaml


dict_yml = [
  {"name" : "Contribute to the CEFI resource list test"},
  {"description" : "The form is designed for user to easily contribute to the CEFI resource list that will be used in the CEFI resource search portal"},
  {"title" : "[CEFI list contribution]: "},
  {"labels" : "cefi_contribution "},
  {"assignees" : ["chiaweh2"]},
  {"body" : [
    {"type" : "markdown"},
    {"attributes" : 
        [{"value" : "Thanks for taking the time to contribute to the CEFI resource list!"}]
    }
    ]},
    {"type" : "input"},
    {"id" : "contact"},
    {"attributes" : 
        [
        {"label": "Contact Details"},
        {"value" : "Thanks for taking the time to contribute to the CEFI resource list!"}]
    }
  ]}
]

with open(r'output.yml', 'w') as file:
    yaml.dump(dict_yml, file)



# body:
#   - type: markdown
#     attributes:
#       value: |
#         Thanks for taking the time to contribute to the CEFI resource list!
#   - type: input
#     id: contact
#     attributes:
#       label: Contact Details
#       description: How can we get in touch with you if we need more info?
#       placeholder: ex. email@example.com
#     validations:
#       required: false
#   - type: textarea
#     id: data-why
#     attributes:
#       label: Tell us a bit about the data/resource!
#       description: Why you think this data worth to be put into the CEFI resource list
#       placeholder: A short sentence or paragraph on why you think the data/resource is important.
#     validations:
#       required: true
#   - type: textarea
#     id: data-title
#     attributes:
#       label: What is the best title for the data/resource?
#       description: A title that best summarize the content.
#       placeholder: Global Marine Heatwaves
#     validations:
#       required: true
#   - type: textarea
#     id: data-institute
#     attributes:
#       label: Who provide this data/resource?
#       description: The institude/university/company that provide this data/resource
#       placeholder: NOAA/PSL
#     validations:
#       required: true
