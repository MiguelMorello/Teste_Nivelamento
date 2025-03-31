<template>
  <div class="app">
    <div class="content">
      <h1>Buscador de Operadoras</h1>
      <div class="input-container">
        <input 
          v-model="registroAns" 
          type="text" 
          placeholder="Digite o código ANS" 
          class="input-field"
        />
      </div>
      <button @click="buscarOperadora" class="btn">Buscar Operadora</button>

      <div v-if="operadora" class="resultado">
        <pre>{{ operadora }}</pre>
      </div>

      <div v-if="erro" class="erro">
        <pre>{{ erro }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      registroAns: "",
      operadora: null,
      erro: null
    };
  },
  methods: {
    async buscarOperadora() {
      this.operadora = null;
      this.erro = null;

      try {
        const response = await axios.get("https://05759f52-858b-4d84-9433-44d5849d1b61-00-2o2xwhcukwp1d.picard.replit.dev/buscar_operadora", {
          params: {
            registro_ans: this.registroAns
          }
        });

        this.operadora = response.data;  // A resposta da API
      } catch (error) {
        if (error.response) {
          this.erro = error.response.data.erro || "Erro desconhecido";
        } else {
          this.erro = "Erro de conexão";
        }
      }
    }
  }
};
</script>

<style scoped>
/* Estilo global */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #007bff;
  color: white;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.app {
  width: 100%;
  max-width: 400px;
  padding: 20px;
  text-align: center;
}

.content {
  background-color: #fff;
  border-radius: 10px;
  padding: 30px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

h1 {
  color: #007bff;
  font-size: 24px;
  margin-bottom: 20px;
}

.input-container {
  margin-bottom: 20px;
}

.input-field {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #007bff;
  margin-bottom: 20px;
}

.btn {
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
  background-color: #007bff;
  border: none;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #0056b3;
}

.resultado,
.erro {
  margin-top: 20px;
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 5px;
  color: #333;
}

.erro {
  background-color: #f8d7da;
  color: #721c24;
}
</style>
