import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')
        url = urlparse(self.path)
        arguments = parse_qs(url.query)

        if self.path == "/":
            contents = read_html_file("index.html").render(context={"n_sequences": len(LIST_SEQUENCES),
                                                                     "genes": LIST_GENES
                                                                     })
            #el render para jinja es como el format para lo normal

        elif self.path == "/ping?":
            contents = read_html_file(self.path[1:-1] + ".html").render()

        elif self.path.startswith("/get?"):
            #&number=value
            #params = "&number=" + str(sequence)
            #ensembl_answer = make_call("/sequence/id", params)
            n_sequence = int(arguments["n_sequence"][0])
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file("get.html").render(context={"n_sequence": n_sequence,
                                                                  "sequence": sequence
                                                                  })

        elif self.path.startswith("/gene?"):
            gene = arguments["gene"][0]
            for g in LIST_GENES:
                if gene == g:
                    sequence = open(FOLDER + gene + ".txt", "r").read()
                    sequence = sequence[sequence.find("\n"):].replace("\n", "")
                    contents = read_html_file("gene.html").render(context={"genename": gene,
                                                                           "gene": sequence
                                                                           })

        elif self.path.startswith("/operation?"):
            sequence = arguments["msg"][0]
            operation = arguments["option"][0]

            if operation == "Info":
                sname, slenght, msg = info(sequence)
                print(msg)
                result = sname + "\n" + slenght + "\n" + msg
                contents = read_html_file("operation.html").render(context={"sequence": sequence,
                                                                            "operationtype": operation,
                                                                            "result": sname
                                                                                      + "\n" + str(msg)})

            elif operation == "Comp":
                comp_seq = complement(sequence)
                contents = read_html_file("operation.html").render(context={"sequence": sequence,
                                                                            "operationtype": operation,
                                                                            "result": comp_seq
                                                                            })

            elif operation =="Rev":
                rev_seq = sequence[::-1]
                contents = read_html_file("operation.html").render(context={"sequence": sequence,
                                                                            "operationtype": operation,
                                                                            "result": rev_seq
                                                                            })

            #info


            #comp

            #return complement_seq

            #reverse

            #contents = read_html_file("operation.html").render(context ={""})




        #elif self.path.startswith("/echo?msg"):
            #message = self.path.split("?msg=")[1]
            #contents = Path("template.html").read_text().format(message.upper())
        else:
            contents = Path("error.html").read_text()



        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()