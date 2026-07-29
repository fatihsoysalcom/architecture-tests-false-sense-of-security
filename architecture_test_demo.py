import unittest

# --- Mock Classes representing different layers ---

class ServiceLayer:
    def __init__(self):
        self.repository = RepositoryLayer()

    def process_data(self):
        # This is a valid dependency for a service
        result = self.repository.get_data()
        print(f"Service processed: {result}")
        return result

class RepositoryLayer:
    def get_data(self):
        # In a real app, this would interact with a DB
        return "data from repo"

class PresentationLayer:
    def __init__(self):
        self.service = ServiceLayer()

    def display_data(self):
        # This is a valid dependency for presentation
        data = self.service.process_data()
        print(f"Displaying: {data}")

# --- Mock Classes representing problematic dependencies ---

class ProblematicServiceLayer:
    def __init__(self):
        # This is an *invalid* direct dependency from Service to Presentation
        # In a real scenario, this might be a direct call to a UI component
        self.presentation = PresentationLayer()

    def perform_action(self):
        print("Problematic service action")
        # This call would violate typical layered architecture rules
        self.presentation.display_data()

# --- Architecture Test Simulation ---

class ArchitectureTests:
    def test_service_does_not_depend_on_presentation(self):
        # This test simulates an architecture rule: ServiceLayer should not directly depend on PresentationLayer.
        # In a real tool like ArchUnit/NetArchTest, this would analyze code structure.
        # Here, we'll manually check for the problematic dependency.
        
        # A 'green' test here would mean no direct dependency is found.
        # However, the *logic* within the service could still cause issues.
        
        # Let's simulate a 'green' test for a valid ServiceLayer
        valid_service = ServiceLayer()
        print("Architecture Test: ServiceLayer -> PresentationLayer (OK - No direct dependency found)")
        assert not hasattr(valid_service, 'presentation'), "ServiceLayer should not have a direct presentation attribute"

        # Now, let's simulate a scenario where the test *passes* but the code is flawed
        # The flaw is not in the direct dependency check, but in the *behavior* of the problematic service.
        print("\n--- Demonstrating the flaw: Test passes, but behavior is wrong ---")
        problematic_service = ProblematicServiceLayer()
        # The architecture test *as defined* would pass if it only checks for direct attribute presence.
        # It wouldn't catch that ProblematicServiceLayer *internally* creates a PresentationLayer instance and calls it.
        print("Architecture Test: ProblematicServiceLayer -> PresentationLayer (Simulated PASS - test logic is too simple)")
        
        # The actual problem: The problematic_service's perform_action method violates the intended flow.
        # The architecture test *didn't catch this logical/behavioral violation*.
        try:
            problematic_service.perform_action() # This call might lead to runtime errors or unexpected behavior in a real app
        except Exception as e:
            print(f"Runtime error encountered due to flawed logic: {e}")


# --- Running the simulation ---

if __name__ == '__main__':
    print("--- Running Architecture Test Simulation ---")
    arch_tester = ArchitectureTests()
    arch_tester.test_service_does_not_depend_on_presentation()
    print("\n--- Simulation finished ---")
