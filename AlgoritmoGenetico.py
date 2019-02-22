#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 09:00:44 2019

@author: robson
"""

from random import random
import matplotlib.pyplot as plt


class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor
        

class Individuo():
    def __init__(self, cromossomo=[]):
        self.nota_avaliacao = 0
        self.melhor_solucao = 0
        self.cromossomo = cromossomo
        
        if not self.cromossomo:
            for i in range(len(lista_produtos)):
                if random() < 0.5:
                    self.cromossomo.append("0")
                else:
                    self.cromossomo.append("1")
        
        self.avaliacao()
                
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        
        for i in range(len(self.cromossomo)):
           if self.cromossomo[i] == '1':
               nota += lista_produtos[i].valor
               soma_espacos += lista_produtos[i].espaco
        if soma_espacos > limite_espaco:
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
    
    def mutacao(self, taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        return self
        

class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.lista_solucoes = []
        self.geracao = 0
        self.melhor_solucao = 0
        
        
    def inicializa_populacao(self):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo())
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
            
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
           soma += individuo.nota_avaliacao
        return soma
    
    def seleciona_pai(self, soma_avaliacao):
        pai = -1
        valor_sorteado = random() * soma_avaliacao
        soma = 0
        i = 0
        
        while i < len(self.populacao) and soma < valor_sorteado:
            soma += self.populacao[i].nota_avaliacao
            pai += 1
            i += 1
        return pai
    
    def crossover(self, pai1, pai2):
        corte = round(random()  * len(pai1.cromossomo))
        
        cromossomo_filho1 = pai1.cromossomo[0:corte] + pai2.cromossomo[corte::]
        cromossomo_filho2 = pai2.cromossomo[0:corte] + pai1.cromossomo[corte::]
        
        filhos = [Individuo(cromossomo_filho1), Individuo(cromossomo_filho2)]
        
        return filhos
    
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        
        print("\nGeraçao: %s" % self.geracao)
        print("Valor: %s" % melhor.nota_avaliacao )
        print("Espaço: %s" % melhor.espaco_usado)
        print("Cromosso %s" % melhor.cromossomo)
    
    def resolver(self, taxa_mutacao, numero_geracoes):
        self.inicializa_populacao()
        
        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)
        
        self.visualiza_geracao()
        
        for geracao in range(numero_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            nova_populacao = []
            
            for individuos_gerados in range(0, self.tamanho_populacao-1, 2):
                pai1 = self.seleciona_pai(soma_avaliacao)
                pai2 = self.seleciona_pai(soma_avaliacao)
                
                filhos = self.crossover(self.populacao[pai1], self.populacao[pai2])
                
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao))
            
            #Elitismo
            nova_populacao.append(self.melhor_solucao)
            self.populacao = list(nova_populacao)
            
            self.ordena_populacao()
            
            self.visualiza_geracao()
            
            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.nota_avaliacao)
            self.melhor_individuo(melhor)
            self.geracao = geracao
      
        print("\n>>>>>>  Melhor solução   <<<<<<<<")
        print("Valor: %s" % self.melhor_solucao.nota_avaliacao )
        print("Espaço: %s" % self.melhor_solucao.espaco_usado)
        print("Cromosso %s" % self.melhor_solucao.cromossomo)
        
        return self.melhor_solucao.cromossomo
        
        
if __name__ == '__main__':
    
    global lista_produtos
    global limite_espaco
    lista_produtos = []
    
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
       
    limite_espaco = 3
    tamanho_populacao = 21
    taxa_mutacao = 0.01
    numero_geracoes = 100
    ag = AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes)
    
    for i in range(len(lista_produtos)):
        if resultado[i] == '1':
            print("Nome: %s R$ %s " % (lista_produtos[i].nome,
                                       lista_produtos[i].valor))
            
    plt.plot(ag.lista_solucoes)
    plt.title("Acompanhamento dos valores")
    plt.show()