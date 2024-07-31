local socket = require("socket")
local http = require("socket.http")
local ltn12 = require("ltn12")
local lxsh = require("lxsh")

-- Function to download a web page
local function download_page(url)
    local response = {}
    local request, code = http.request{
        url = url,
        sink = ltn12.sink.table(response)
    }
    
    if code ~= 200 then
        return nil, "Error: " .. code
    end
    
    return table.concat(response)
end

-- Function to parse HTML
local function parse_html(html)
    local parsed = lxsh.html(html)
    return parsed
end

-- Function to render HTML (very basic, just prints text content)
local function render_html(parsed)
    for _, node in ipairs(parsed) do
        if type(node) == "table" then
            if node.tag == "title" then
                print("Title: " .. node[1])
            elseif node.tag == "p" or node.tag == "h1" or node.tag == "h2" or node.tag == "h3" then
                print(node[1])
            end
        end
    end
end

-- Main browser function
local function browse(url)
    print("Loading " .. url)
    local html, err = download_page(url)
    if not html then
        print(err)
        return
    end
    
    local parsed = parse_html(html)
    render_html(parsed)
end

-- Simple command-line interface
while true do
    io.write("Enter URL (or 'quit' to exit): ")
    local input = io.read()
    if input == "quit" then
        break
    end
    browse(input)
end
