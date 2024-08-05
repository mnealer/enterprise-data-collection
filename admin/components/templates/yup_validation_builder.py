class SchemaManager:
    def __init__(self):
        self.schemas = {}

    # Add a schema
    def add_schema(self, schema_name, **fields):
        # Store the schema fields
        self.schemas[schema_name] = fields

    # Generate JS code to load schemas
    def render(self):
        # Add Yup library
        content = '<script src="https://cdnjs.cloudflare.com/ajax/libs/yup/0.32.9/yup.min.js"></script>'

        # Add schemas
        content += '<script>\n'
        content += 'var schemas = {};\n'

        # Generate JS code for each schema
        for schema_name, fields in self.schemas.items():
            content += f'schemas["{schema_name}"] = yup.object().shape({{'
            for field_name, field_type in fields.items():
                content += f'"{field_name}": yup.{field_type}().required(),'
            content = content.rstrip(',')
            content += '});\n'

        # Close script tag
        content += '</script>'

        return content


schema_manager = SchemaManager()
schema_manager.add_schema("userSchema", name="string", email="string")
schema_manager.add_schema("postSchema", title="string", content="string")

generated_script = schema_manager.render()
