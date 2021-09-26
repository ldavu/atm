using System;
using System.Threading;

namespace devop
{
    class Program
    {
        static void Main(string[] args)
        {
            string RestarProgram = "y";
            int chances = 3;
            int saldo = 2500;
            string NomeCliente = "Orivaldo";
            int senha = 1234;

            while(chances >= 0)
            {
                Console.WriteLine("Digite sua senha:\n");
                if(senha == 1234)
                {
                    Console.WriteLine($"Bem vindo {NomeCliente}");
                    Thread.Sleep(1);
                    Console.WriteLine("presione 1 para ver o saldo no banco");
                    Console.WriteLine("Presione 2 para retirar um valor");
                    Console.WriteLine("Presione 3 para depositar um valor");
                    var Ler_Linha = Convert.ToInt32(Console.ReadLine());

                    switch (Ler_Linha)
                    {
                        case 1:
                            Console.WriteLine($"{NomeCliente}");
                            Console.WriteLine($"Seu saldo é de {saldo}");
                            Thread.Sleep(2);

                            Console.WriteLine("Sair do programar?");
                            Console.ReadLine();

                            if (Console.ReadLine() == "Y")
                            {
                                Console.WriteLine("Saiu!");
                                break;
                            }
                            continue;

                        case 2:
                            Console.WriteLine("")
                    }
                }

            }
        }
    }
}
