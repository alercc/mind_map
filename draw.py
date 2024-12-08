from pandas import read_excel, ExcelFile
from pyvis.network import Network
import webbrowser
from sys import argv
import pdb

def wrap_text(text, words_per_line):
    words = text.split()
    wrapped_lines = []
    for i in range(0, len(words), words_per_line):
        line = " ".join(words[i:i+words_per_line])
        wrapped_lines.append(line)
    return "\n".join(wrapped_lines)

def chart(file,wrap,layout):
    for sheet in ExcelFile(file).sheet_names:
        df = read_excel(io = file, sheet_name = sheet, header = None)
        title = df.iloc[0,0]
        df = df.iloc[3:,]
        df.columns = ['source','target']
        unicos = list(set(df.stack()))
        net = Network(directed=True)
        for u in range(len(unicos)):
            net.add_node(u, label = wrap_text(unicos[u],wrap), shape = "box")
        for index, row in df.iterrows():
            id_origem = unicos.index(row['source'])
            id_destino = unicos.index(row['target'])
            net.add_edge(id_origem, id_destino)
        if layout == 'hierarchical':
            net.set_options(""" var options = { "layout": { "hierarchical": { "enabled": true, "levelSeparation": 200, "nodeSpacing": 200, "treeSpacing": 300, "blockShifting": true, "edgeMinimization": true, "parentCentralization": true } }, "physics": { "hierarchicalRepulsion": { "nodeDistance": 200 } } } """)
        if layout == 'forceAtlas2Based':
            net.set_options(""" var options = { "physics": { "forceAtlas2Based": { "gravitationalConstant": -50, "springLength": 200, "springConstant": 0.05 }, "minVelocity": 0.75, "solver": "forceAtlas2Based" } } """)
        html_content = net.generate_html()
        title_html = "<h1 style='text-align: center;'>" + title + "</h1>\n"
        modified_html = html_content.replace("<body>", f"<body>\n{title_html}")
        with open(sheet+".html", "w", encoding='utf-8') as the_file:
            the_file.write(modified_html)


if __name__ == "__main__":

    chart(
        file = argv[1],
        wrap = 3,
        layout = 'forceAtlas2Based'
        )
