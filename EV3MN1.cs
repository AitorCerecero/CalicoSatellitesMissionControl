
//DATOS ENTRADA
double[] x = {3,4 };
double[] y = { 23.5,30 };

double xA = 1.5, yA = 0;
//Variables del programa
int datos = x.Length; //Cantidad de elementos en X
double[,] matriz = new double[datos, datos + 1];

//RECORRER MATRIZ (CUADRADA)
for (int i = 0; i < datos; i++) //RENGLONES
{
    for (int j = 0; j < datos; j++) //COLUMNAS
    { //EL PRIMER VALOR DE X SE ELEVA A LA 0 , 1, 2 ,3, 4, 5
        matriz[i, j] = Math.Pow(x[i], j);
    }
}

//VACIAR EL VECTOR Y EN LA ULTIMA COLUMNA DE LA MATRIZ.
for (int i = 0; i < datos; i++)
{
    matriz[i, datos] = y[i];
}

int ren = datos, col = ren + 1;
//VARIABLES FIJAS
double factor, pivote;

// Recorrer matriz para imprimir datos
for (int r = 0; r < ren; r++) //RECORRER RENGLONES r = 0 -> 1 -> 2
{
    pivote = matriz[r, r];
    for (int c = 0; c < col; c++) //RECORRER COLUMNAS C = 0 
    {
        //   if(matriz[r,c]==0)
        matriz[r, c] = matriz[r, c] / pivote;
        //  matriz[r,c] /= pivote;   
    }
    //VOLVER A RECORRER LA MATRIZ PARA HACER LAS CONVERSIONES A CERO
    for (int rCero = 0; rCero < ren; rCero++)
    {
        if (r != rCero) //BRINCAR EL RENGLON DEL PIVOTE
        {
            factor = matriz[rCero, r];

            for (int cCero = 0; cCero < col; cCero++)
            {
                //(VALOR ORIGINAL ) – (RENGLON DEL PIVOTE,C)(FACTOR))\
                matriz[rCero, cCero] = matriz[rCero, cCero] - (factor * matriz[r, cCero]);
                //matriz[rCero, cCero] -= (factor* matriz[r,cCero]);
            }
        }
    }
}
//imprimir en formar en ecuación
for (int r = 0; r < ren; r++)
{
    if (r < ren - 1)
    {
        Console.Write("La ecuacion es: "+matriz[r, col - 1] + "x^" + r + " + ");
    }
    else
    {
        Console.Write(matriz[r, col - 1] + "x^" + r);
    }
}

