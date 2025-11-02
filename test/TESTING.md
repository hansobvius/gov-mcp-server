# Testing Guide for Brazilian Government MCP Server

This guide explains how to test your MCP (Model Context Protocol) server that provides tools for searching Brazilian congressional deputies.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Tests
```bash
# Run comprehensive test suite
python test/test_comprehensive.py

# Run individual API tests
python test/test_deputies_api.py

# Run MCP server tests
python test/test_mcp_server.py
```

## Test Files Overview

| File | Purpose |
|------|---------|
| `test/test_comprehensive.py` | Complete test suite with all functionality |
| `test/test_api.py` | Tests API functions independently |
| `test/test_mcp_server.py` | Tests MCP server and tools integration |

## What Each Test Covers

### API Tests (`test/test_api.py`)
- **Deputies Search**: Tests searching deputies by name
- **Deputy Details**: Tests retrieving detailed information about specific deputies
- **Error Handling**: Tests various edge cases and error conditions

### MCP Server Tests (`test/test_mcp_server.py`)
- **Tool Registration**: Verifies MCP tools are properly registered
- **Tool Execution**: Tests the actual MCP tool functions
- **Server Initialization**: Ensures the MCP server starts correctly

### Comprehensive Tests (`test/test_comprehensive.py`)
- **Import Validation**: Ensures all modules can be imported
- **Manifest Validation**: Validates `manifest.json` structure
- **API Connectivity**: Tests connection to Brazilian government API
- **Search Functionality**: Tests various search scenarios
- **Details Retrieval**: Tests deputy details functionality
- **MCP Integration**: Tests complete MCP tool workflow

## Manual Testing

### Test the MCP Server Directly
```bash
# Start the MCP server
python src/main.py
```

The server will run in stdio mode and wait for MCP protocol messages.

### Test with MCP Client
If you have an MCP client (like Claude Desktop), you can:
1. Add this server to your MCP configuration
2. Use the `get_deputies_by_names_tool` tool
3. Search for deputies by name

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure you're running tests from the project root
   - Check that all dependencies are installed

2. **API Connection Issues**
   - Verify internet connectivity
   - Check if the Brazilian government API is accessible
   - The API endpoint is: `https://dadosabertos.camara.leg.br/api/v2`

3. **MCP Tool Not Working**
   - Ensure the tool is properly registered in `src/mcp/tools.py`
   - Check that the function signature matches MCP requirements

### Debug Mode
Add debug prints to understand what's happening:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Expected Test Results

When all tests pass, you should see:
- All imports successful
- Manifest validation passed
- API connectivity confirmed
- Search functionality working
- Deputy details retrieval working
- MCP tool execution successful

## Customizing Tests

### Adding New Test Cases
Edit the test files to add your own test scenarios:

```python
# In test/test_comprehensive.py
async def test_custom_functionality(self):
    """Test your custom functionality"""
    # Your test code here
    pass
```

### Testing Different API Endpoints
Modify the API test functions to test different government data endpoints.

## Test Output Example

```
[START] Starting Comprehensive MCP Server Tests
==================================================

[TEST] Testing Imports...
[PASS] Import: Config module
[PASS] Import: Main module
...

[TEST] Testing API Connectivity...
[PASS] API Connectivity API responded successfully

TEST SUMMARY
==================================================
Total Tests: 8
Passed: 8
Failed: 0
Success Rate: 100.0%
==================================================
```

## Next Steps

After running tests successfully:
1. Deploy your MCP server
2. Configure it with MCP clients
3. Start using the deputy search functionality
4. Consider adding more government data sources

## Additional Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Brazilian Government Open Data](https://dadosabertos.camara.leg.br/)
- [FastMCP Library](https://github.com/jlowin/fastmcp)
