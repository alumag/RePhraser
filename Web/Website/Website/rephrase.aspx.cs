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
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void btnsave_Click(object sender, EventArgs e)
        {
            StringBuilder sb = new StringBuilder();

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
                        Process process = new Process();
                        // Configure the process using the StartInfo properties.
                        process.StartInfo.FileName = @"python";
                        process.StartInfo.Arguments = @"C:\Users\Viole\Documents\Magshimim\Project\Synonym\ParseSentence.py -f " + @"C:\Users\Viole\Documents\Magshimim\Project\Web\Website\Website\texts\" + FileUpload1.FileName;
                        //process.StartInfo.WindowStyle = ProcessWindowStyle.Maximized;
                        process.OutputDataReceived += Process_OutputDataReceived;
                        process.Start();
                        process.BeginOutputReadLine();
                        process.WaitForExit();// Waits here for the process to exit.          
                    }
                    catch (Exception ex)
                    {
                        sb.Append("<br/> Error <br/>");
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
            lblmessage.Text = e.Data.ToString();
        }
    }
}