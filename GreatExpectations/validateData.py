from great_expectations.core import ExpectationSuite, ExpectationConfiguration
from great_expectations.checkpoint import SimpleCheckpoint
from great_expectations.data_context import DataContext

# Create a simple ExpectationSuite with an expectation
suite = ExpectationSuite(expectation_suite_name="my_suite")
suite.add_expectation(
    ExpectationConfiguration(
        expectation_type="expect_table_row_count_to_be_between",
        kwargs={
            "min_value": 2,
            "max_value": 10,
        },
        meta={
            "notes": "We expect the table to have between 2 and 10 rows."
        }
    )
)

# Save the suite
suite.save()

# Create a Checkpoint
context = DataContext()
checkpoint = SimpleCheckpoint(
    name="my_checkpoint",
    data_context=context,
    batches=[
        {
            "batch_kwargs": {
                "path": r"C:\Users\sushma.n\OneDrive - Incedo Technology Solutions Ltd\Desktop\Assignments\GreatExpectations\data\testData.csv"  # Replace with your data file path
            },
            "expectation_suite_names": ["my_suite"]
        }
    ]
)

# Run the checkpoint and generate HTML report
results = checkpoint.run()

# Generate HTML report
report = results[0].to_json_dict()["result"]["details"]

# Save the report to an HTML file
with open("data_validation_report.html", "w") as f:
    f.write(report)