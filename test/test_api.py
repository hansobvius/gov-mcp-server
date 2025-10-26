#!/usr/bin/env python3
"""
Test script for the Brazilian Government MCP Server API functions
"""
import asyncio
import sys
import os

# Add src to path so we can import modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from api.deputies.deputies_api import get_deputados_by_name, get_deputados_details


async def test_deputies_by_name():
    """Test searching deputies by name"""
    print("🔍 Testing get_deputados_by_name...")
    
    # Test with a common name
    result = await get_deputados_by_name("eduardo")
    print(f"✅ Search for 'eduardo': {len(result.get('dados', [])) if result else 0} results")
    
    if result and 'dados' in result:
        print(f"   First result: {result['dados'][0].get('nome', 'N/A')}")
    
    # Test with empty name
    result_empty = await get_deputados_by_name("")
    print(f"✅ Search for empty string: {len(result_empty.get('dados', [])) if result_empty else 0} results")
    
    # Test with non-existent name
    result_nonexistent = await get_deputados_by_name("xyz123nonexistent")
    print(f"✅ Search for non-existent name: {len(result_nonexistent.get('dados', [])) if result_nonexistent else 0} results")


async def test_deputy_details():
    """Test getting deputy details by ID"""
    print("\n🔍 Testing get_deputados_details...")
    
    # Test with a known deputy ID (using first result from previous test)
    result = await get_deputados_by_name("eduardo")
    if result and 'dados' in result and len(result['dados']) > 0:
        deputy_id = result['dados'][0]['id']
        print(f"   Testing with deputy ID: {deputy_id}")
        
        details = await get_deputados_details(deputy_id)
        if details:
            print(f"✅ Deputy details retrieved: {details.get('dados', {}).get('nome', 'N/A')}")
        else:
            print("❌ Failed to retrieve deputy details")
    else:
        print("⚠️  No deputies found to test details function")


async def main():
    """Run all tests"""
    print("🚀 Starting Brazilian Government MCP Server API Tests\n")
    
    try:
        await test_deputies_by_name()
        await test_deputy_details()
        print("\n✅ All tests completed!")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
