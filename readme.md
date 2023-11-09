> This package is a work in progress.

A simple Python module to replace "dumb quotes" with "smart quotes" in HTML. It handles both single and double quotes.

It has no dependencies except for Python's standard library.

# Example input and output

```html
<p>This is a "test".</p>
<p>'This' is a 'test'.</p>
<p>This isn't a test.</p>
<p>He said, "Don't let others suffer for your hatred."</p>
```

> This is a “test”.  
‘This’ is a ‘test’.  
This isn’t a test.  
He said, “Don’t let others suffer for your hatred.”

converts to

```html
<p>This is a &ldquo;test&rdquo;.</p>
<p>&lsquo;This&rsquo; is a &lsquo;test&rsquo;.</p>
<p>This isn&rsquo;t a test.</p>
<p>He said, &ldquo;Don&rsquo;t let others suffer for your hatred.&rdquo;</p>
```

> <p>This is a &ldquo;test&rdquo;.</p><p>&lsquo;This&rsquo; is a &lsquo;test&rsquo;.</p><p>This isn&rsquo;t a test.</p><p>He said, &ldquo;Don&rsquo;t let others suffer for your hatred.&rdquo;</p>

# Usage

Once installed with `pip`, use it like this:

```py
import smarties
html = open("my.html").read()
smart_quoted_html = smarties.smartquote(html)
```

You can also use `smartify` from the command line:

```
smartify <input_file> <output_file>
```

If no output file is provided, output is sent to `stdout`.

# License

MIT