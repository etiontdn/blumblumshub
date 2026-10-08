# 1. Parâmetros
p = 18899
q = 19163
n = p * q

s = 1234567

# 2. Inicialização
x0 = (s ** 2) % n
xi = x0

num_bits = 100000
bits = []

for _ in range(num_bits):
  xi = (xi ** 2) % n
  bit = xi % 2 
  bits.append(str(bit))

# 3. Salvar os bits em um arquivo de texto para a suíte NIST
sequencia_binaria = "".join(bits)
with open("bbs_sequencia.txt", "w") as f:
  f.write(sequencia_binaria)

print(f"Módulo n calculado: {n}")
print(f"Sequência de {num_bits} bits gerada e salva com sucesso!")