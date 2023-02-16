public class Aula11_relogio_ponto{
	public static void main(String[]args){
		ControlePonto cp = new ControlePonto();
		//Objeto Gerente
		Gerente g = new Gerente();
		g.setMatricula(1);
		g.setNome("Guilherme");
		//Objeto Secretaria
		Secretario s = new Secretario();
		g.setMatricula(2);
		g.setNome("Cristina");
		//Objeto  Telefonista
		Telefonista t = Telefonista;
		g.setMatricula(32);
		g.setNome("Pedro");
		cp.registraEntrada(g);
		cp.registraEntrada(s);
		cp.registraEntrada(t);
		cp.registraSaida(t);
		cp.registraSaida(s);
		cp.registraSaida(g);
		g.almocar("Macarrão");
	}
}
