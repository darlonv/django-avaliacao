from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.colors import pink, black, red, blue, green
from reportlab.lib.units import cm
from PIL import Image
import PIL


FILENAME = "pdf/abc.pdf"


def getGrid(x_list, y_list):
    grid = []

    for j in range(len(y_list) - 1):
        row = []
        for i in range(len(x_list) - 1):
            pos = (x_list[i], y_list[j])
            row.append(pos)
        grid.append(row)

    return grid


def getGridLists(
    n_rows=4,
    n_cols=4,
    width=1,
    height=1,
    left_border=1,
    upper_border=1,
    right_border=1,
    bottom_border=1,
    pagesize=A4,
):
    w, h = pagesize

    x_list = []
    try:
        x = left_border * cm
        for i in range(n_cols + 1):
            if x >= (w - right_border):
                print("Cuidado: largura da página excedida.")

            x_list.append(x)
            x += width * cm

        y_list = []
        y = h - upper_border * cm
        for i in range(n_rows + 1):
            if y <= bottom_border:
                print("Cuidado: altura da página excedida.")
            y_list.append(y)
            y -= height * cm
    except:
        pass

    return x_list, y_list


def pdfGridPrintTrabalhos(
    grid,
    trabalhos,
    xlist,
    ylist,
    print_grid=True,
    font="Times-Roman",
    fontsize=14,
    borda_esq=5,
    borda_cima=14,
    alt_linha=14,
    filename=FILENAME,
    pagesize=A4,
):
    # font = "Times-Roman"
    # fontsize = 25
    # alt_linha = fontsize
    # borda_cima = alt_linha
    # borda_esq = 5

    # Calcula o número de páginas

    # Percorre para cada página

    try:
        w, h = pagesize
        pdf = canvas.Canvas(filename, pagesize=pagesize)

        if print_grid:
            pdf.grid(xlist, ylist)

        pdf.setFillColor(black)
        pdf.setFont(font, fontsize)
        # pos = grid[0][0]
        # pdf.circle(pos[0], pos[1], 0.5 * cm, fill=1)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if counter >= len(trabalhos):
                    break
                pos = grid[i][j]
                # print(pos)
                trabalho = trabalhos[counter]
                l = 0
                for k in range(len(trabalho)):
                    # print(counter, k)
                    pdf.setFillColor(black)
                    pdf.setFont(font, fontsize)
                    if type(trabalho[k]) == str:
                        pdf.drawString(
                            pos[0] + borda_esq,
                            pos[1] - borda_cima - l * alt_linha,
                            trabalho[k],
                        )
                        l += 1
                    else:
                        # print("oi")
                        # pdf.drawString(
                        #     pos[0] + trabalho[k][0],
                        #     pos[1] - trabalho[k][1],
                        #     trabalho[k][2],
                        # )
                        pdf.drawInlineImage(
                            trabalho[k][2],
                            pos[0] + trabalho[k][0],
                            pos[1] - trabalho[k][1],
                            preserveAspectRatio=True,
                        )

                counter += 1
            if counter >= len(trabalhos):
                break

        # pdf.drawImage(im1, 0, 0, preserveAspectRatio=True)
        # pdf.drawInlineImage(im1, 0, 0, preserveAspectRatio=True)

        pdf.save()
    except Exception as e:
        print("Error:", e)


def pdfEtiquetas(
    n_linhas,
    n_colunas,
    largura,
    altura,
    itens,
    print_grid=True,
    font="Times-Roman",
    fontsize=14,
    borda_esq=5,
    borda_cima=14,
    alt_linha=14,
    filename=FILENAME,
    pagesize=A4,
):
    x_list, y_list = getGridLists(n_linhas, n_colunas, largura, altura)
    grid = getGrid(x_list, y_list)

    pdfGridPrintTrabalhos(
        grid,
        itens,
        x_list,
        y_list,
        print_grid=print_grid,
        font=font,
        fontsize=fontsize,
        borda_esq=borda_esq,
        borda_cima=borda_cima,
        alt_linha=alt_linha,
    )


def main():
    # print(getGrid(4, 4, 2, 2))
    # x_list, y_list = getGridLists(9, 3, 5, 3)
    # pdfTestGrid(x_list, y_list)

    # grid = getGrid(x_list, y_list)
    # print(grid)
    # pdfTestGrid(x_list, y_list, grid)

    im1 = Image.open("./001.png")
    im1 = im1.resize((100, 100))
    trabalhos = []

    for i in range(13):
        trabalhos.append(
            [f"Titulo: Trabalho {i}", f"Autores: {i} e {i+1}", [120, 110, im1]]
        )

    # trabalhos = [
    #     ["abc", "a", "qr1"],
    #     ["def", "d", "qr2", "oioi", [50, 110, im1]],
    #     ["ghi", "g", "qr test", [50, 110, im1]],
    # ]

    n_linhas = 7
    n_colunas = 2
    largura = 8
    altura = 4

    pdfEtiquetas(
        n_linhas, n_colunas, largura, altura, trabalhos, filename="pdf/abc.pdf"
    )
    # pdfGridPrintTrabalhos(grid, trabalhos, x_list, y_list)

    # print(getGridLists(4, 4, 2, 2))


if __name__ == "__main__":
    main()
