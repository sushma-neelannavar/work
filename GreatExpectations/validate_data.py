import pandas as pd
from great_expectations.dataset import PandasDataset
from great_expectations import DataContext

# Load sample data into a Pandas DataFrame
data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 32, 45, 28, 19]
}

df = pd.DataFrame(data)

# Convert the DataFrame to a PandasDataset
my_dataset = PandasDataset(df)

# Create expectations
my_dataset.expect_column_values_to_be_in_set("name", ["Alice", "Bob", "Charlie", "David", "Eve"])

# Save the expectations to a JSON file
my_dataset.save_expectation_suite("my_suite")


# Load the data context
context = DataContext("great_expectations/")

# Load the expectations suite
suite = context.get_expectation_suite("my_suite")

# Validate the data using the suite
batch_kwargs = {"dataset": df}
results = context.run_validation_operator(
    "action_list_operator",
    assets_to_validate=[batch_kwargs],
    run_id="validate_data"
)

# Generate an HTML report
validation_results = [result for batch in results for result in batch["results"]]
html_report = context.validation_operator.render_full_static_site(
    validation_results,
    run_info_at_end=True
)
report_file_path = "validation_report.html"
with open(report_file_path, "w") as f:
    f.write(html_report)

print(f"Validation report generated: {report_file_path}")