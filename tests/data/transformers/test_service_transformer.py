from unittest import mock
from unittest.mock import mock_open

file_content = "20801;102980;6847973;1;1;0;Ouessant"


@mock.patch("data.transformers.service_transformer.map_code_to_name", return_value="Orange")
def test_extract_should_store_extracted_value_to_data(map_code_to_name, service_transformer):
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        service_transformer._extract()
        assert service_transformer.data == {"ouessant": {"Orange": {"2G": True, "3G": True, "4G": False}}}


@mock.patch("data.transformers.service_transformer.map_code_to_name")
def test_extract_should_store_extracted_value_of_same_region_in_same_key(map_code_to_name, service_transformer):
    map_code_to_name.side_effect = ["Orange", "SFR"]
    content = "20801;102980;6847973;1;1;0;Ouessant\n20802;102980;6847973;1;1;0;Ouessant"
    with mock.patch('builtins.open', mock.mock_open(read_data=content)):
        service_transformer._extract()
        assert service_transformer.data == {
            "ouessant": {"Orange": {"2G": True, "3G": True, "4G": False}, "SFR": {"2G": True, "3G": True, "4G": False}}}


@mock.patch("data.transformers.service_transformer.map_code_to_name")
def test_extract_should_lower_case_key_of_network_provider(map_code_to_name, service_transformer):
    map_code_to_name.side_effect = ["Orange"]
    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
        service_transformer._extract()
        assert list(service_transformer.data.keys())[0] == "ouessant"


@mock.patch("data.transformers.service_transformer.map_code_to_name", return_value="Orange")
def test_save_should_write_to_output_file(map_code_to_name, service_transformer):
    content = {"quessant": {"Orange": {"2G": True, "3G": True, "4G": False}}}
    service_transformer.data = content
    open_mock = mock_open()
    with mock.patch("builtins.open", open_mock, create=True):
        service_transformer._save()
    open_mock.assert_called_with("output_file", "w")


@mock.patch("data.transformers.service_transformer.map_code_to_name", return_value="Orange")
@mock.patch("data.transformers.service_transformer.ServiceTransformer._extract")
@mock.patch("data.transformers.service_transformer.ServiceTransformer._save")
def test_transform_should_transform_data(save_func, extract_func, map_code_to_name, service_transformer):
    service_transformer.transform()
    save_func.assert_called_once()
    extract_func.assert_called_once()
