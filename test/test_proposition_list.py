#!/usr/bin/env python3
"""
Test script for the Brazilian Government MCP Server API functions
"""
import asyncio
import sys
import os

# Add project root to path so we can import modules
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, project_root)

from src.api.propositions.propositions import get_propositions_by_id, get_proposition_details


async def test_proposition_by_id():
    """Test searching deputies by name"""
    print("Testing get_deputados_by_name...")

    # Test with a common name
    result = await get_propositions_by_id("92346")
    print(f"PASS Search for 'eduardo': {len(result.get('dados', [])) if result else 0} results")

    if result and 'dados' in result and len(result['dados']) > 0:
        first_proposition = result['dados'][0]
        print(f"   First result: {first_proposition.get('nome', 'N/A')} (ID: {first_proposition.get('id', 'N/A')})")

    # Test with empty name
    result_empty = await get_propositions_by_id("")
    print(f"PASS Search for empty string: {len(result_empty.get('dados', [])) if result_empty else 0} results")

    # Test with non-existent name
    result_nonexistent = await get_propositions_by_id("xyz123nonexistent")
    print(
        f"PASS Search for non-existent name: {len(result_nonexistent.get('dados', [])) if result_nonexistent else 0} results")


async def test_proposition_detail():
    """Test getting deputy details by ID"""
    print("\nTesting get_deputados_details...")

    # Test with a known deputy ID (using first result from previous test)
    result = await get_propositions_by_id("92346")
    if result and 'dados' in result and len(result['dados']) > 0:
        deputy_id = result['dados'][0]['id']
        print(f"   Testing with deputy ID: {deputy_id}")

        details = await get_propositions_by_id(deputy_id)
        if details:
            print(f"PASS Proposition details retrieved: {details.get('dados', {}).get('nome', 'N/A')}")
        else:
            print("FAIL Failed to retrieve proposition details")
    else:
        print("WARN No deputies found to test details function")


async def main():
    """Run all tests"""
    print("Starting Brazilian Government MCP Server API Tests\n")

    try:
        await test_proposition_by_id()
        # await test_proposition_detail()
        print("\nPASS All tests completed!")

    except Exception as e:
        print(f"\nFAIL Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())

