
import java.util.ArrayList;
import javax.swing.JOptionPane;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author nakamura
 */
class Conta{
    private int nro;
    private String tipo;
    private float saldo;
    public Conta(int nro, String tipo, float saldo){
        this.nro=nro;
        this.tipo=tipo;
        this.saldo=saldo;
    }//construtor
    public int getNro(){
        return this.nro;
    }
    public String getTipo(){
        return this.tipo;
    }
    public float getSaldo(){
        return this.saldo;
    }
    public void depositar(float valor){
        this.saldo+=valor;
    }
    public boolean sacar(float valor){
        if(valor > this.saldo) return false;
        this.saldo-=valor;
        return true;
    }
    public boolean transferir(float valor, Conta destino){
        if(this.sacar(valor)){
            destino.depositar(valor);
            return true;
        }
        else return false;
    }
}//Conta

class Cliente{
    private String nome, CPF, endereco, telefone;
    private Conta conta;
    public Cliente (String nome, String CPF, String endereco, 
                    String telefone, Conta conta){
        this.nome=nome;
        this.CPF=CPF;
        this.endereco=endereco;
        this.telefone=telefone;
        this.conta=conta;
    }
    public String getNome(){
        return this.nome;
    }
    public String getCPF(){
        return this.CPF;
    }
    public String getEndereco(){
        return this.endereco;
    }
    public String getTelefone(){
        return this.telefone;
    }
    public Conta getConta(){
        return this.conta;
    }
}//Cliente
class Banco{
    private ArrayList<Cliente> clientes;
    public Banco(){
        this.clientes=new ArrayList<Cliente>();
    }
    public void cadastrar(Cliente c){
        this.clientes.add(c);
    }
    public Cliente consultar(String nome){
        for(Cliente c: this.clientes)
            if(c.getNome().equals(nome))
                return c;
        return null;
    }//consultar
    public boolean depositar(String nome, float valor){
     Cliente c=this.consultar(nome);
     if(c==null) return false;
     c.getConta().depositar(valor);
     return true;
    }//depositar
    public boolean sacar(String nome, float valor){
        Cliente c=this.consultar(nome);
        if(c==null) return false;
        return c.getConta().sacar(valor);
    }//sacar
    public boolean transferir(String origem, String destino,
                                            float valor){
        Cliente c1=this.consultar(origem);
        Cliente c2=this.consultar(destino);
        if(c1==null || c2==null) return false;
        return c1.getConta().transferir(valor, c2.getConta());
    }
}//Banco

public class Trabalho {
    public static void main(String args[]){
        Banco b=new Banco();
        String menu[]={"Cadastrar", "Consultar", "Depositar", 
                       "Sacar", "Transferir", "Finalizar"};
        String opcao="";
        do{
            opcao=JOptionPane.showInputDialog(null, "Selecione uma opção", "Banco", JOptionPane.INFORMATION_MESSAGE, null, menu, menu[5]).toString();
            switch(opcao){
                case "Cadas6trar": cadastrar(b); break;
                case "Consultar": consultar(b); break;
                case "Depositar": depositar(b); break;
                case "Sacar": sacar(b); break;
                case "Transferir": transferir(b); break;
            }
        }while(!opcao.equals("Finalizar"));
    }
    
    private static void cadastrar(Banco b){
        String nome=JOptionPane.showInputDialog("Nome do cliente");
        String CPF=JOptionPane.showInputDialog("CPF");
        String endereco=JOptionPane.showInputDialog("Endereço");
        String telefone=JOptionPane.showInputDialog("Telefone");
        int nro=Integer.parseInt(
                       JOptionPane.showInputDialog("Nro da conta"));
        String tipo[]={"conta corente", "conta poupança"};
        String tipoConta=JOptionPane.showInputDialog(null, "Selecione uma opção", "Banco", JOptionPane.INFORMATION_MESSAGE, null, tipo, tipo[0]).toString();
        float saldo=Float.parseFloat(
                       JOptionPane.showInputDialog("Saldo inicial"));
        b.cadastrar(new Cliente(nome, CPF, endereco, telefone, 
                                new Conta(nro, tipoConta, saldo)));
    }//cadastrar
    private static void consultar(Banco b){
        String nome=JOptionPane.showInputDialog("Informe o nome do cliente para consulta");
        Cliente c=b.consultar(nome);
        if(c!=null)
            JOptionPane.showMessageDialog(null, "Nome: "+c.getNome()+
                                 "\nNro da conta: "+c.getConta().getNro()+
                                 "\nTipo: "+c.getConta().getTipo()+
                                 "\nSaldo atual: "+c.getConta().getSaldo());
        else JOptionPane.showMessageDialog(null, "Cliente "+nome+" não cadastrado!");
    }//consultar
    private static void depositar(Banco b){
        String nome=JOptionPane.showInputDialog("Informe o nome do cliente para depósito");
        float valor=Float.parseFloat(
                    JOptionPane.showInputDialog("Valor do depósito"));
        if(b.depositar(nome, valor))
            JOptionPane.showMessageDialog(null, "Depósito realizado!");
        else JOptionPane.showMessageDialog(null, "Conta não cadastada!");
    }//depositar
    private static void sacar(Banco b){
        String nome=JOptionPane.showInputDialog("Informe o nome do cliente para saque");
        float valor=Float.parseFloat(
                    JOptionPane.showInputDialog("Valor do saque"));
        if(b.sacar(nome, valor))
            JOptionPane.showMessageDialog(null, "Saque realizado!");
        else JOptionPane.showMessageDialog(null, "Falha no saque!");
    }//sacar
    private static void transferir(Banco b){
        String origem=JOptionPane.showInputDialog("cliente da conta origem");
        String destino=JOptionPane.showInputDialog("cliente da conta destino");
        float valor=Float.parseFloat(
                    JOptionPane.showInputDialog("Valor da transferêcia"));
        if(b.transferir(origem, destino, valor))
            JOptionPane.showMessageDialog(null, "Transferência realizada!");
        else JOptionPane.showMessageDialog(null, "Falha na transferência!");
    }//transferir
}
