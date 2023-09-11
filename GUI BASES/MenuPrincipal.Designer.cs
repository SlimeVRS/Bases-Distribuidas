namespace GUI_BASES
{
    partial class MenuPrincipal
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MenuPrincipal));
            this.label1 = new System.Windows.Forms.Label();
            this.dataGridView1 = new System.Windows.Forms.DataGridView();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.flowLayoutPanel2 = new System.Windows.Forms.FlowLayoutPanel();
            this.panelSubMenuRegistrar = new System.Windows.Forms.Panel();
            this.label2 = new System.Windows.Forms.Label();
            this.panel1 = new System.Windows.Forms.Panel();
            this.label3 = new System.Windows.Forms.Label();
            this.btnLibros = new System.Windows.Forms.Button();
            this.btnUsuarios = new System.Windows.Forms.Button();
            this.btnLector = new System.Windows.Forms.Button();
            this.CerrarSesion = new System.Windows.Forms.Button();
            this.btnPrestar = new System.Windows.Forms.Button();
            this.btnDevolverLibro = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.flowLayoutPanel2.SuspendLayout();
            this.panelSubMenuRegistrar.SuspendLayout();
            this.panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.label1.Font = new System.Drawing.Font("Lucida Handwriting", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.White;
            this.label1.Location = new System.Drawing.Point(248, 44);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(628, 31);
            this.label1.TabIndex = 11;
            this.label1.Text = "SISTEMA ADMINISTRACION DE BIBLIOTECA";
            // 
            // dataGridView1
            // 
            this.dataGridView1.AllowUserToAddRows = false;
            this.dataGridView1.AllowUserToDeleteRows = false;
            this.dataGridView1.AllowUserToResizeColumns = false;
            this.dataGridView1.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridView1.Location = new System.Drawing.Point(242, 111);
            this.dataGridView1.Name = "dataGridView1";
            this.dataGridView1.RowHeadersVisible = false;
            this.dataGridView1.Size = new System.Drawing.Size(715, 461);
            this.dataGridView1.TabIndex = 13;
            // 
            // groupBox1
            // 
            this.groupBox1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(86)))), ((int)(((byte)(141)))));
            this.groupBox1.Controls.Add(this.flowLayoutPanel2);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Location = new System.Drawing.Point(34, 112);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(192, 460);
            this.groupBox1.TabIndex = 14;
            this.groupBox1.TabStop = false;
            // 
            // flowLayoutPanel2
            // 
            this.flowLayoutPanel2.Controls.Add(this.panelSubMenuRegistrar);
            this.flowLayoutPanel2.Controls.Add(this.label2);
            this.flowLayoutPanel2.Controls.Add(this.panel1);
            this.flowLayoutPanel2.Location = new System.Drawing.Point(4, 64);
            this.flowLayoutPanel2.Name = "flowLayoutPanel2";
            this.flowLayoutPanel2.Size = new System.Drawing.Size(186, 334);
            this.flowLayoutPanel2.TabIndex = 14;
            // 
            // panelSubMenuRegistrar
            // 
            this.panelSubMenuRegistrar.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(86)))), ((int)(((byte)(141)))));
            this.panelSubMenuRegistrar.Controls.Add(this.btnLibros);
            this.panelSubMenuRegistrar.Controls.Add(this.btnUsuarios);
            this.panelSubMenuRegistrar.Controls.Add(this.btnLector);
            this.panelSubMenuRegistrar.Location = new System.Drawing.Point(3, 3);
            this.panelSubMenuRegistrar.Name = "panelSubMenuRegistrar";
            this.panelSubMenuRegistrar.Size = new System.Drawing.Size(180, 147);
            this.panelSubMenuRegistrar.TabIndex = 8;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.ForeColor = System.Drawing.Color.White;
            this.label2.Location = new System.Drawing.Point(3, 153);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(169, 25);
            this.label2.TabIndex = 14;
            this.label2.Text = "OPERACIONES";
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.CerrarSesion);
            this.panel1.Controls.Add(this.btnPrestar);
            this.panel1.Controls.Add(this.btnDevolverLibro);
            this.panel1.Location = new System.Drawing.Point(3, 181);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(179, 150);
            this.panel1.TabIndex = 11;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(64)))), ((int)(((byte)(86)))), ((int)(((byte)(141)))));
            this.label3.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 15F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.ForeColor = System.Drawing.Color.White;
            this.label3.Location = new System.Drawing.Point(29, 16);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(134, 25);
            this.label3.TabIndex = 16;
            this.label3.Text = "REGISTRAR";
            // 
            // btnLibros
            // 
            this.btnLibros.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btnLibros.FlatAppearance.BorderSize = 0;
            this.btnLibros.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Coral;
            this.btnLibros.FlatAppearance.MouseOverBackColor = System.Drawing.Color.OrangeRed;
            this.btnLibros.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnLibros.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnLibros.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.btnLibros.Image = ((System.Drawing.Image)(resources.GetObject("btnLibros.Image")));
            this.btnLibros.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnLibros.Location = new System.Drawing.Point(2, 2);
            this.btnLibros.Name = "btnLibros";
            this.btnLibros.Size = new System.Drawing.Size(175, 47);
            this.btnLibros.TabIndex = 4;
            this.btnLibros.Text = "Libros";
            this.btnLibros.UseVisualStyleBackColor = false;
            this.btnLibros.Click += new System.EventHandler(this.btnLibros_Click);
            // 
            // btnUsuarios
            // 
            this.btnUsuarios.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btnUsuarios.FlatAppearance.BorderSize = 0;
            this.btnUsuarios.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Coral;
            this.btnUsuarios.FlatAppearance.MouseOverBackColor = System.Drawing.Color.OrangeRed;
            this.btnUsuarios.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnUsuarios.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnUsuarios.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.btnUsuarios.Image = ((System.Drawing.Image)(resources.GetObject("btnUsuarios.Image")));
            this.btnUsuarios.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnUsuarios.Location = new System.Drawing.Point(2, 50);
            this.btnUsuarios.Name = "btnUsuarios";
            this.btnUsuarios.Size = new System.Drawing.Size(175, 47);
            this.btnUsuarios.TabIndex = 3;
            this.btnUsuarios.Text = "Usuarios";
            this.btnUsuarios.UseVisualStyleBackColor = false;
            this.btnUsuarios.Click += new System.EventHandler(this.btnUsuarios_Click);
            // 
            // btnLector
            // 
            this.btnLector.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btnLector.FlatAppearance.BorderSize = 0;
            this.btnLector.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Coral;
            this.btnLector.FlatAppearance.MouseOverBackColor = System.Drawing.Color.OrangeRed;
            this.btnLector.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnLector.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnLector.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.btnLector.Image = ((System.Drawing.Image)(resources.GetObject("btnLector.Image")));
            this.btnLector.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnLector.Location = new System.Drawing.Point(2, 98);
            this.btnLector.Name = "btnLector";
            this.btnLector.Size = new System.Drawing.Size(175, 47);
            this.btnLector.TabIndex = 5;
            this.btnLector.Text = "Lectores";
            this.btnLector.UseVisualStyleBackColor = false;
            // 
            // CerrarSesion
            // 
            this.CerrarSesion.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.CerrarSesion.FlatAppearance.BorderSize = 0;
            this.CerrarSesion.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Coral;
            this.CerrarSesion.FlatAppearance.MouseOverBackColor = System.Drawing.Color.OrangeRed;
            this.CerrarSesion.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.CerrarSesion.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CerrarSesion.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.CerrarSesion.Image = ((System.Drawing.Image)(resources.GetObject("CerrarSesion.Image")));
            this.CerrarSesion.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.CerrarSesion.Location = new System.Drawing.Point(2, 99);
            this.CerrarSesion.Name = "CerrarSesion";
            this.CerrarSesion.Size = new System.Drawing.Size(175, 47);
            this.CerrarSesion.TabIndex = 9;
            this.CerrarSesion.Text = "Log Out";
            this.CerrarSesion.UseVisualStyleBackColor = false;
            this.CerrarSesion.Click += new System.EventHandler(this.CerrarSesion_Click);
            // 
            // btnPrestar
            // 
            this.btnPrestar.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btnPrestar.FlatAppearance.BorderSize = 0;
            this.btnPrestar.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Coral;
            this.btnPrestar.FlatAppearance.MouseOverBackColor = System.Drawing.Color.OrangeRed;
            this.btnPrestar.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnPrestar.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnPrestar.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.btnPrestar.Image = ((System.Drawing.Image)(resources.GetObject("btnPrestar.Image")));
            this.btnPrestar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnPrestar.Location = new System.Drawing.Point(2, 3);
            this.btnPrestar.Name = "btnPrestar";
            this.btnPrestar.Size = new System.Drawing.Size(175, 47);
            this.btnPrestar.TabIndex = 6;
            this.btnPrestar.Text = "Prestar";
            this.btnPrestar.UseVisualStyleBackColor = false;
            this.btnPrestar.Click += new System.EventHandler(this.btnPrestar_Click);
            // 
            // btnDevolverLibro
            // 
            this.btnDevolverLibro.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.btnDevolverLibro.FlatAppearance.BorderSize = 0;
            this.btnDevolverLibro.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Coral;
            this.btnDevolverLibro.FlatAppearance.MouseOverBackColor = System.Drawing.Color.OrangeRed;
            this.btnDevolverLibro.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnDevolverLibro.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnDevolverLibro.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.btnDevolverLibro.Image = ((System.Drawing.Image)(resources.GetObject("btnDevolverLibro.Image")));
            this.btnDevolverLibro.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnDevolverLibro.Location = new System.Drawing.Point(2, 51);
            this.btnDevolverLibro.Name = "btnDevolverLibro";
            this.btnDevolverLibro.Size = new System.Drawing.Size(175, 47);
            this.btnDevolverLibro.TabIndex = 7;
            this.btnDevolverLibro.Text = "Devolver";
            this.btnDevolverLibro.UseVisualStyleBackColor = false;
            this.btnDevolverLibro.Click += new System.EventHandler(this.btnDevolverLibro_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = global::GUI_BASES.Properties.Resources.logo_tec;
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(230, 94);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 12;
            this.pictureBox1.TabStop = false;
            // 
            // MenuPrincipal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.RoyalBlue;
            this.ClientSize = new System.Drawing.Size(978, 622);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.dataGridView1);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.label1);
            this.Name = "MenuPrincipal";
            this.Text = "Menu Principal";
            ((System.ComponentModel.ISupportInitialize)(this.dataGridView1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.flowLayoutPanel2.ResumeLayout(false);
            this.flowLayoutPanel2.PerformLayout();
            this.panelSubMenuRegistrar.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.DataGridView dataGridView1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.FlowLayoutPanel flowLayoutPanel2;
        private System.Windows.Forms.Panel panelSubMenuRegistrar;
        private System.Windows.Forms.Button btnLibros;
        private System.Windows.Forms.Button btnUsuarios;
        private System.Windows.Forms.Button btnLector;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button CerrarSesion;
        private System.Windows.Forms.Button btnPrestar;
        private System.Windows.Forms.Button btnDevolverLibro;
        private System.Windows.Forms.Label label3;
    }
}