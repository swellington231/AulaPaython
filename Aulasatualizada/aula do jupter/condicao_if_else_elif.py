{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7bb5e533",
   "metadata": {},
   "source": [
    "Aula 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c5087c44",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Olá Mundo!\n"
     ]
    }
   ],
   "source": [
    "print (\"Olá Mundo!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a77c3290",
   "metadata": {},
   "source": [
    "#Crinado e somando duas variaveis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "45e03bd1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15 3.14\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = 3\n",
    "b = 5\n",
    "\n",
    "\n",
    "a = 10\n",
    "b = 5\n",
    "pi= 3.14\n",
    "\n",
    "print ( a + b, pi)\n",
    "type(a)\n",
    "type (pi)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "50c4aedd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "curso de python!\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a = (\"curso de python!\")\n",
    "print(a)\n",
    "type(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e207044e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou muito feliz com o curso de python\n",
      "poissempre fui apaixonado por essa aréa!\n",
      "com fé em Deus vou seguir carreira nela\n"
     ]
    }
   ],
   "source": [
    "a = \"\"\"Estou muito feliz com o curso de python\n",
    "poissempre fui apaixonado por essa aréa!\n",
    "com fé em Deus vou seguir carreira nela\"\"\"\n",
    "\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "32580acd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hahaha\n"
     ]
    }
   ],
   "source": [
    "print (\"ha\"*3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c772bd1f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'rs'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "nome = \"Curso\"\n",
    "#nome[4]\n",
    "nome[2:4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "e69d3b3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "bool"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    " curso = True\n",
    "print(curso)\n",
    "type(curso)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c46a9589",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Digite um numero: 155\n",
      "155\n"
     ]
    }
   ],
   "source": [
    "x = input(\"Digite um numero: \")\n",
    "print(x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "b433136c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Digite o nome do curso DESEMVOLVEDOR PYTHON PROFISSÃO DO FUTURO\n",
      "Você digitou DESEMVOLVEDOR PYTHON PROFISSÃO DO FUTURO\n",
      "DESEMVOLVEDOR PYTHON PROFISSÃO DO FUTURO é a profissão do futudo e minha paixão\n"
     ]
    }
   ],
   "source": [
    "nome = input(\"Digite o nome do curso \")\n",
    "print(\"Você digitou %s\" % nome)\n",
    "print(\"%s é a profissão do futudo e minha paixão\"% nome)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "93f42e12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "false, 0 não é maior que 10\n"
     ]
    }
   ],
   "source": [
    "x = 0 \n",
    "y = 10\n",
    "\n",
    "if x > y:\n",
    "\n",
    "    print (\"sim\")\n",
    "else:\n",
    "\n",
    "    print(\"false, 0 não é maior que 10\")\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f3242a72",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "0af8f5e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "if x and y:\n",
    "    \n",
    "    print(\"sim\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "bbd894b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sim\n"
     ]
    }
   ],
   "source": [
    "if x or y:\n",
    "\n",
    "    print(\"sim\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "fcaed82a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes\n"
     ]
    }
   ],
   "source": [
    "if 'py' in 'python':\n",
    "     print('yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "fcd161f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "yes\n"
     ]
    }
   ],
   "source": [
    "if 'João' in ['Pedro', 'João', 'Maria']:\n",
    "    print('yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "0c286184",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Meu nome não JOão\n"
     ]
    }
   ],
   "source": [
    "nome = \"João\"\n",
    "sobre_nome = \"José\"\n",
    "ultimoNome = \"Santos\"\n",
    "if nome ==\"Wellington\":\n",
    "    print(\"Wellington\")\n",
    "    if sobre_nome ==\"José\":\n",
    "        print(\"josé\")\n",
    "        if ultimoNome == \"Santos\":\n",
    "            print(\"Santos\")\n",
    "            \n",
    "        else:\n",
    "            print(\"Meu ultimo nome não é santos\")\n",
    "    else:\n",
    "        print(\"Meu segundo nome não é José\")\n",
    "else:\n",
    "    print(\"Meu nome não JOão\")\n",
    "    \n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "03dedcbf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Meu curso não existe na universidade\n"
     ]
    }
   ],
   "source": [
    "curso = \"html\"\n",
    "\n",
    "if curso == \"java\":\n",
    "    print(\"Meu  é java\")\n",
    "    \n",
    "elif curso == \"javascript\":\n",
    "    print(\"Meu curso é java scrtip\")\n",
    "    \n",
    "elif curso == \"python\":\n",
    "    print(\"Meu curso é python\")\n",
    "    \n",
    "else:\n",
    "    print(\"Meu curso não existe na universidade\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "58bac3ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b é maior que  a\n"
     ]
    }
   ],
   "source": [
    "a = 25\n",
    "b = 30\n",
    "\n",
    "if b > a:\n",
    "    print(\"b é maior que  a\")\n",
    "elif a == b:\n",
    "    print(\" a é igual b\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d440cfea",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
