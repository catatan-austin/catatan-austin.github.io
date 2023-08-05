import sys
import markdown

def read_markdown_file(filename):
    with open(filename, 'r') as f:
        print('read input')
        return f.read()

def read_html_template(filename):
    with open(filename, 'r') as f:
        print('read template')
        return f.read()

def write_html_file(content, filename):
    with open(filename, 'w') as f:
        f.write(content)
        print('write content')

def generate_html(markdown_content, html_template):
    title = markdown_content.split('\n')[0].replace('**', '').strip()
    post_html = markdown.markdown('\n'.join(markdown_content.split('\n')[1:]))
    print('generate html')
    return html_template.format(title=title, post=post_html)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} input.md output.html')
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    markdown_content = read_markdown_file(input_filename)
    html_template = read_html_template('template.html')
    html_content = generate_html(markdown_content, html_template)
    write_html_file(html_content, output_filename)