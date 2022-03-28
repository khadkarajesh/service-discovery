from unittest import mock
from unittest.mock import mock_open


def test_extract_should_store_extracted_value_to_data(name_transformer):
    file_content = "MCC,MNC3,Operator,Code\n208,1,Orange,20801"
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        name_transformer._extract()
        assert name_transformer.data == {"20801": "Orange"}


def test_extract_should_replace_parenthesis_present_in_name(name_transformer):
    file_content = "MCC,MNC3,Operator,Code\n208,1,Orange(Best Telecom),20801"
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        name_transformer._extract()
        assert name_transformer.data == {"20801": "Orange"}


def test_save_should_write_to_output_file(name_transformer):
    file_content = {"20801": "Orange"}
    name_transformer.data = file_content
    open_mock = mock_open()
    with mock.patch("builtins.open", open_mock, create=True):
        name_transformer._save()
    open_mock.assert_called_with("output_file", "w")


@mock.patch("data.transformers.name_transformer.NameTransformer._extract")
@mock.patch("data.transformers.name_transformer.NameTransformer._save")
def test_transform_should_transform_data(save_func, extract_func, name_transformer):
    name_transformer.transform()
    save_func.assert_called_once()
    extract_func.assert_called_once()
