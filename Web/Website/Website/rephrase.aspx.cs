using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Website
{
    public partial class rephrase : System.Web.UI.Page
    {
        StringBuilder sb = new StringBuilder();
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnsave_Click(object sender, EventArgs e)
        {
            sb.Clear();

            if (FileUpload1.HasFile)
            {
                try
                {
                    sb.AppendFormat(" Uploading file: {0}", FileUpload1.FileName);

                    //saving the file
                    FileUpload1.SaveAs(@"C:\Users\Viole\Documents\Magshimim\Project\Web\Website\Website\texts\" + FileUpload1.FileName);

                    //Showing the file information
                    sb.AppendFormat("<br/> Save As: {0}", FileUpload1.PostedFile.FileName);
                    sb.AppendFormat("<br/> File type: {0}", FileUpload1.PostedFile.ContentType);
                    sb.AppendFormat("<br/> File length: {0}", FileUpload1.PostedFile.ContentLength);
                    sb.AppendFormat("<br/> File name: {0}", FileUpload1.PostedFile.FileName);
                    lblmessage.Text = sb.ToString();

                    try
                    {
                        //run_process(@"C:\Users\Viole\Documents\Magshimim\Project\Web\Website\Website\texts\" + FileUpload1.FileName);
                        Process process = new Process();
                        // Configure the process using the StartInfo properties.
                        process.StartInfo.FileName = @"cmd.exe";
                        process.StartInfo.WindowStyle = ProcessWindowStyle.Minimized;
                        process.OutputDataReceived += Process_OutputDataReceived;
                        process.StartInfo.Arguments = ("exit()");
                        process.Start();
                        //process.StartInfo.Arguments = (@"python C:\Users\Viole\Documents\Magshimim\Project\Synonym\ParseSentence.py -f " + @"C:\Users\Viole\Documents\Magshimim\Project\Web\Website\Website\texts\" + FileUpload1.FileName);
                        process.BeginOutputReadLine();
                        string stderr = process.StandardError.ReadToEnd();
                        string stdout = process.StandardOutput.ReadToEnd();
                        sb.AppendFormat("Errors: {0}<br/>", stderr);
                        sb.AppendFormat("Output: {0}<br/>", stdout);
                        lblmessage.Text = sb.ToString();
                        process.WaitForExit(); // Waits here for the process to exit.          
                    }
                    catch (Exception ex)
                    {
                        sb.Append("<br/> Error: python<br/>");
                        sb.AppendFormat("Unable to run algorthem <br/> {0}", ex.Message);
                        lblmessage.Text = sb.ToString();
                    }
                }
                catch (Exception ex)
                {
                    sb.Append("<br/> Error <br/>");
                    sb.AppendFormat("Unable to save file <br/> {0}", ex.Message);
                    lblmessage.Text = sb.ToString();
                }
            }
            else
            {
                lblmessage.Text = sb.ToString();
            }
        }

        private void Process_OutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            sb.Append(e.Data.ToString());
            lblmessage.Text = sb.ToString();
        }

        private void run_process(string file)
        {
            ProcessStartInfo startInfo = new ProcessStartInfo();
            startInfo.UseShellExecute = false; //required to redirect standart input/output

            // redirects on your choice
            startInfo.RedirectStandardOutput = true;
            startInfo.RedirectStandardOutput = true;
            startInfo.RedirectStandardError = true;

            startInfo.FileName = "cmd.exe";
            startInfo.Arguments = "";

            Process process = new Process();
            process.StartInfo = startInfo;
            process.Start();

            process.StandardInput.WriteLine(@"python C:\Users\Viole\Documents\Magshimim\Project\Synonym\ParseSentence.py -f " + file);

        }
    }
}