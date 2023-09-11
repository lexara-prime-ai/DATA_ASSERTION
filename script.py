import great_expectations as ge

# Initialize Data Context
context = ge.data_context.DataContext("./data.csv")

# Create Expectation Suite
batch_kwargs = {
    "datasource": "",
    "batch_kwargs": {
        "data_asset_name": "",
        "data_connector_name": "",
        "path": "",
        "reader_method": "read_csv"
    },
}

suite = context.create_expectation_suite("", overwrite_existing=True)

# Add expectations to suite
suite.expect_column_values_to_not_be_null(column="name")
suite.expect_column_values_to_not_be_null(column="age", min_value=0)
suite.expect_column_values_to_not_be_null(column="city")

# Save expectation suite
context.save_expectation_suite(suite, "<PATH>")

# Validate data
batch = context.get_batch(batch_kwargs, suite)
results = context.run_validation_operator(
    "action_list_operator",
    assets_to_validate=[batch]
)

# Display validation results
print(results)
