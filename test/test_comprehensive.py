#!/usr/bin/env python3
"""
Comprehensive test suite for the Brazilian Government MCP Server
"""
import asyncio
import sys
import os
import json
import subprocess
import time

# Add project root to path so we can import modules
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, project_root)


class MCPTester:
    def __init__(self):
        self.test_results = []
    
    def log_test(self, test_name, success, message=""):
        """Log test result"""
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if message:
            print(f"    {message}")
        self.test_results.append((test_name, success, message))
    
    async def test_api_connectivity(self):
        """Test API connectivity"""
        print("\n🔍 Testing API Connectivity...")
        
        try:
            from src.api.deputies.deputies_api import get_deputados_by_name
            
            # Test with a simple query
            result = await get_deputados_by_name("test")
            
            if result is not None:
                self.log_test("API Connectivity", True, "API responded successfully")
                return True
            else:
                self.log_test("API Connectivity", False, "API returned None")
                return False
                
        except Exception as e:
            self.log_test("API Connectivity", False, f"Exception: {e}")
            return False
    
    async def test_deputies_search(self):
        """Test deputies search functionality"""
        print("\n🔍 Testing Deputies Search...")
        
        try:
            from src.api.deputies.deputies_api import get_deputados_by_name
            
            # Test cases
            test_cases = [
                ("eduardo", "Common name search"),
                ("", "Empty string search"),
                ("xyz123", "Non-existent name search"),
                ("a", "Single character search")
            ]
            
            all_passed = True
            
            for query, description in test_cases:
                try:
                    result = await get_deputados_by_name(query)
                    
                    if result is not None:
                        count = len(result.get('dados', []))
                        self.log_test(f"Search: {description}", True, f"Found {count} results")
                    else:
                        self.log_test(f"Search: {description}", False, "Returned None")
                        all_passed = False
                        
                except Exception as e:
                    self.log_test(f"Search: {description}", False, f"Exception: {e}")
                    all_passed = False
            
            return all_passed
            
        except Exception as e:
            self.log_test("Deputies Search", False, f"Import error: {e}")
            return False
    
    async def test_deputy_details(self):
        """Test deputy details functionality"""
        print("\n🔍 Testing Deputy Details...")
        
        try:
            from src.api.deputies.deputies_api import get_deputados_by_name, get_deputados_details
            
            # Get a deputy ID first
            result = await get_deputados_by_name("eduardo")
            
            if result and 'dados' in result and len(result['dados']) > 0:
                deputy_id = result['dados'][0]['id']
                
                # Test getting details
                details = await get_deputados_details(deputy_id)
                
                if details and 'dados' in details:
                    self.log_test("Deputy Details", True, f"Retrieved details for deputy {deputy_id}")
                    return True
                else:
                    self.log_test("Deputy Details", False, "Details returned None or invalid format")
                    return False
            else:
                self.log_test("Deputy Details", False, "No deputies found to test details")
                return False
                
        except Exception as e:
            self.log_test("Deputy Details", False, f"Exception: {e}")
            return False
    
    async def test_mcp_tool(self):
        """Test MCP tool functionality"""
        print("\n🔍 Testing MCP Tool...")
        
        try:
            from src.mcp.tools import get_deputies_by_names_tool
            
            # Test the tool
            result = await get_deputies_by_names_tool("eduardo")
            
            if result and result != 'Result not generated':
                self.log_test("MCP Tool", True, "Tool executed successfully")
                return True
            else:
                self.log_test("MCP Tool", False, f"Tool returned: {result}")
                return False
                
        except Exception as e:
            self.log_test("MCP Tool", False, f"Exception: {e}")
            return False
    
    def test_imports(self):
        """Test all imports"""
        print("\n🔍 Testing Imports...")
        
        imports_to_test = [
            ("src.config", "Config module"),
            ("src.main", "Main module"),
            ("src.api.api", "API module"),
            ("src.api.deputies.deputies_api", "Deputies API module"),
            ("src.mcp.tools", "MCP tools module"),
            ("src.mcp.project_tools.deputies_tools", "Deputies tools module")
        ]
        
        all_passed = True
        
        for module, description in imports_to_test:
            try:
                __import__(module)
                self.log_test(f"Import: {description}", True)
            except Exception as e:
                self.log_test(f"Import: {description}", False, f"Error: {e}")
                all_passed = False
        
        return all_passed
    
    def test_manifest(self):
        """Test manifest.json validity"""
        print("\n🔍 Testing Manifest...")
        
        try:
            manifest_path = os.path.join(os.path.dirname(__file__), '..', 'manifest.json')
            with open(manifest_path, 'r') as f:
                manifest = json.load(f)
            
            required_fields = ['name', 'version', 'server', 'mcp_config']
            missing_fields = [field for field in required_fields if field not in manifest]
            
            if not missing_fields:
                self.log_test("Manifest Validation", True, f"All required fields present")
                return True
            else:
                self.log_test("Manifest Validation", False, f"Missing fields: {missing_fields}")
                return False
                
        except Exception as e:
            self.log_test("Manifest Validation", False, f"Error: {e}")
            return False
    
    def print_summary(self):
        """Print test summary"""
        print("\n" + "="*50)
        print("📊 TEST SUMMARY")
        print("="*50)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for _, success, _ in self.test_results if success)
        failed_tests = total_tests - passed_tests
        
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if failed_tests > 0:
            print("\n❌ Failed Tests:")
            for test_name, success, message in self.test_results:
                if not success:
                    print(f"  - {test_name}: {message}")
        
        print("="*50)


async def main():
    """Run comprehensive tests"""
    print("🚀 Starting Comprehensive MCP Server Tests")
    print("="*50)
    
    tester = MCPTester()
    
    # Run all tests
    tester.test_imports()
    tester.test_manifest()
    await tester.test_api_connectivity()
    await tester.test_deputies_search()
    await tester.test_deputy_details()
    await tester.test_mcp_tool()
    
    # Print summary
    tester.print_summary()


if __name__ == "__main__":
    asyncio.run(main())
