using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace GUI_BASES
{
    public partial class MenuPrincipal : Form
    {
        public MenuPrincipal()
        {
            InitializeComponent();
        }

        private void CerrarSesion_Click(object sender, EventArgs e)
        {
            LoginUsuarios loginForm = new LoginUsuarios();
            loginForm.Show();
            this.Hide();
        }

        private void btnLibros_Click(object sender, EventArgs e)
        {
            Libros Fl = new Libros();
            this.Hide();
            Fl.Show();
        }

        private void btnUsuarios_Click(object sender, EventArgs e)
        {
            Usuarios Usuarios = new Usuarios();
            Usuarios.Show();
            this.Hide();
        }

        private void btnPrestar_Click(object sender, EventArgs e)
        {
            Prestamos prestamos = new Prestamos();
            this.Hide();
            prestamos.Show(); 
        }

        private void btnDevolverLibro_Click(object sender, EventArgs e)
        {
            Devoluciones devoluciones = new Devoluciones();
            this.Hide();
            devoluciones.Show();
        }
    }
}
