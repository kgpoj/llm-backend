import json
from data_fields import data_fields
from chains import RelevantFieldsChain, ConversationChain

class Jarvis:
    def __init__(self):
        self.relevant_fields_chain = RelevantFieldsChain.from_llm()
        self.conversation_chain = ConversationChain.from_llm()

    def _format_data(self, data):
        data = self._remove_typename(data)
        return json.dumps(data).replace('{', '<').replace('}', '>').replace('\'', '').replace('\"', '')

    def _remove_typename(self, data):
        if isinstance(data, dict):
            return {
                key: self._remove_typename(value) for key, value in data.items() if key != '__typename'
            }
        elif isinstance(data, list):
            return [self._remove_typename(item) for item in data]
        return data

    def _extract_relevant_data(self, attrs, data):
        results = {}
        for attr_path in attrs:
            attr_path = attr_path.replace('\'', '').replace('\"', '')
            results[attr_path] = self._get_value_by_path(attr_path, data)
        return results

    @staticmethod
    def _get_value_by_path(attr_path, data):
        value = data
        for key in attr_path.split('.'):
            try:
                value = value[key]
            except (KeyError, TypeError):
                if value == data:
                    value = None
        return value

    def respond_to_question(self, question, data):
        relevant_fields = self.relevant_fields_chain.predict_and_parse(question=question,
                                                                       data_fields=data_fields)
        relevant_data = self._extract_relevant_data(relevant_fields, data)

        formatted_relevant_data = self._format_data(relevant_data)
        response = self.conversation_chain.run(question=question,
                                               data_fields=data_fields,
                                               data=formatted_relevant_data)
        return response
