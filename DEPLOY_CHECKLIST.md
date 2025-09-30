# 📋 CHECKLIST - Deploy Streamlit Cloud

## ✅ Passos para Deploy:

### 1. Acessar Streamlit Cloud
- [ ] Ir para: https://share.streamlit.io
- [ ] Fazer login com conta GitHub
- [ ] Clicar em "New app"

### 2. Configurar Deploy
- [ ] **Repository:** seu-usuario/plano-comercial-daniel-esteves
- [ ] **Branch:** main
- [ ] **Main file path:** streamlit_app.py
- [ ] Clicar em "Deploy!"

### 3. Aguardar Deploy
- [ ] Streamlit Cloud irá instalar dependências automaticamente
- [ ] Processo leva cerca de 2-5 minutos
- [ ] URL será criada automaticamente

### 4. Sua URL será algo como:
- https://plano-comercial-daniel-esteves-[hash].streamlit.app
- OU pode personalizar para: https://esteves.streamlit.app (se disponível)

## ⚠️ IMPORTANTE:
Antes do deploy funcionar 100%, você precisa configurar o banco de dados (Passo 4).

## 🔧 Se der erro:
1. Verificar se todos os arquivos foram enviados para GitHub
2. Verificar se requirements.txt está correto
3. Configurar banco de dados nas settings