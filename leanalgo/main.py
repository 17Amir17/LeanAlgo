#!/usr/bin/env python

"""Main entry point for the LeanAlgo application."""

import json
from leanalgo.models import UserData, AlgorithmResult


def create_sample_user() -> UserData:
    """Create a sample user with Pydantic validation."""
    user = UserData(
        id=1,
        name="John Doe",
        email="john.doe@example.com",
        tags=["user", "premium"],
        description="A sample user"
    )
    return user


def run_sample_algorithm() -> AlgorithmResult:
    """Run a sample algorithm and return results."""
    # This simulates running an algorithm
    return AlgorithmResult(
        algorithm_name="SampleSort",
        execution_time_ms=42.5,
        success=True,
        data={"sorted_items": 100, "comparisons": 450}
    )


def main():
    """Main entry point for the application."""
    print("Welcome to LeanAlgo!")
    print("This is a Python project with Pydantic models.")
    
    # Create and display a sample user
    user = create_sample_user()
    print("\nSample User:")
    print(json.dumps(user.model_dump(), indent=2))
    
    # Run a sample algorithm and display results
    result = run_sample_algorithm()
    print("\nAlgorithm Result:")
    print(json.dumps(result.model_dump(), indent=2))


if __name__ == "__main__":
    main() 