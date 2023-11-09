def smartquote(html):
    in_html_tag = False
    in_quote = False
    last_was_blank = False

    html = (html.replace('&ldquo;','"')
        .replace('&rdquo;','"')
        .replace('&lsquo;',"'")
        .replace('&rsquo;',"'")
        .replace("‘","'")
        .replace("’","'")
        .replace("“",'"')
        .replace("”",'"')
    )

    formatted = []

    for idx, c in enumerate(html):

        if c in {"<",">"}:
            in_html_tag = not in_html_tag
            formatted.append(c)
            continue

        if in_html_tag:
            try:

                # A paragraph break is assumed to close quotes.
                if html[idx:idx+2].lower() in {"p ","p>"}:
                    last_was_blank = True
                    in_quote = False
                elif html[idx:idx+2].lower() in {"p/>"}:
                    last_was_blank = True
                    in_quote = False
                elif html[idx:idx+3].lower() in {"br ","br>","br/", "hr ", "hr/", "ul ", "li ", "ul/", "li/"}:
                    last_was_blank = True
                elif html[idx:idx+4].lower() in {"br/>", "hr/>", "div ", "div/"}:
                    last_was_blank = True

            except IndexError:
                last_was_blank = False
            formatted.append(c)
            continue
        
        else:            
            if c == "'":
                if last_was_blank:
                    formatted.append("&lsquo;")
                    last_was_blank = False
                else:
                    formatted.append("&rsquo;")
                continue
            
            elif c == '"':
                if in_quote:
                    formatted.append("&rdquo;")
                else:
                    formatted.append("&ldquo;")
                in_quote = not in_quote
                continue
                
        last_was_blank = c in {" ", "&nbsp;"}
        formatted.append(c)
            
    new_html = "".join(formatted)
    
    return new_html

def cmdline():
    import sys
    from pathlib import Path

    if len(sys.argv)<2:
        print("No input file specified", file=sys.stderr)
        sys.exit(1)

    input_file = Path(sys.argv[1])
    if not input_file.exists():
        print(f"Input file {input_file} not valid", file=sys.stderr)
        sys.exit(1)

    output_file = None

    if len(sys.argv)>2:
        output_file = Path(sys.argv[2])
        
    data = input_file.read_text(encoding="utf8")
    quoted = smartquote(data)

    if output_file:
        with open(output_file, "w", encoding="utf8") as f:
            f.write(quoted)
    else:
        print(quoted)