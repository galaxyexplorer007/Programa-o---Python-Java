import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

const App = () => {
  const [nome, setNome] = useState('');
  const [saudacao, setSaudacao] = useState('');

  const obterSaudacao = () => {
    const hora = new Date().getHours();
    if (hora < 12) return 'Um Bom dia';
    if (hora < 18) return 'Uma Boa tarde';
    return 'Uma Boa noite';
  };

  const atualizarSaudacao = () => {
    if (nome.trim()) {
      setSaudacao(`${obterSaudacao()}, ${nome}! Bem-vindo(a)!`);
    }
  };

  const limparSaudacao = () => {
    setNome('');
    setSaudacao('');
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Escreva o seu nome:</Text>
      <TextInput
        style={styles.input}
        placeholder="Seu nome"
        placeholderTextColor="#ccc"
        value={nome}
        onChangeText={setNome}
      />
      <TouchableOpacity style={styles.button} onPress={atualizarSaudacao}>
        <Text style={styles.buttonText}>Atualizar</Text>
      </TouchableOpacity>
      <TouchableOpacity style={[styles.button, styles.buttonDelete]} onPress={limparSaudacao}>
        <Text style={styles.buttonText}>Limpar</Text>
      </TouchableOpacity>
      {saudacao !== '' && <Text style={styles.saudacao}>{saudacao}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#265D80',
    padding: 20,
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#FFF',
    marginBottom: 10,
  },
  input: {
    width: '80%',
    height: 40,
    borderWidth: 1,
    borderColor: '#000000',
    borderRadius: 5,
    paddingLeft: 10,
    color: '#FFF',
    backgroundColor: 'rgba(0, 0, 0, 0.2)',
    marginBottom: 15,
  },
  button: {
    backgroundColor: '#807E26',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 5,
    marginTop: 5,
  },
  buttonDelete: {
    backgroundColor: '#552828',
  },
  buttonText: {
    color: '#FFF',
    fontWeight: 'bold',
  },
  saudacao: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#000000',
    textAlign: 'center',
    marginTop: 20,
  },
});

export default App;