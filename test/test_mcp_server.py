#!/usr/bin/env python3
"""
Test script for the MCP Server functionality
"""
import asyncio
import sys
import os
import json

# Add project root to path so we can import modules
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, project_root)

import src.config as config
import src.tools.deputies_tools as deputies_tools


async def test_mcp_tool():
    """Test the MCP tool directly"""
    print("[TEST] Testing MCP tool: get_deputies_by_names_tool...")
    
    try:
        # Test the tool function
        result = await deputies_tools.get_deputies_by_names_tool("eduardo")
        print(f"[SUCCESS] Tool executed successfully")
        print(f"   Result type: {type(result)}")
        print(f"   Result length: {len(str(result))} characters")
        
        # Try to parse as JSON if it's a string
        if isinstance(result, str):
            try:
                parsed = json.loads(result)
                print(f"   Parsed JSON with {len(parsed.get('dados', []))} deputies")
            except json.JSONDecodeError:
                print(f"   Result is not JSON: {result[:100]}...")
        
    except Exception as e:
        print(f"[ERROR] Tool test failed: {e}")
        import traceback
        traceback.print_exc()


async def test_mcp_server_initialization():
    """Test MCP server initialization"""
    print("\n[TEST] Testing MCP server initialization...")
    
    try:
        # Use the top-level imported `config.mcp`
        print(f"[SUCCESS] MCP server initialized: {config.mcp.name}")
        print(f"   Server type: {type(config.mcp)}")

        # Check if tools are registered
        if hasattr(config.mcp, 'tools'):
            print(f"   Registered tools: {len(config.mcp.tools) if config.mcp.tools else 0}")

    except Exception as e:
        print(f"[ERROR] Server initialization failed: {e}")
        import traceback
        traceback.print_exc()


async def main():
    """Run MCP tests"""
    print("[START] Starting MCP Server Tests\n")
    
    await test_mcp_server_initialization()
    await test_mcp_tool()
    
    print("\n[SUCCESS] MCP tests completed!")


if __name__ == "__main__":
    asyncio.run(main())
