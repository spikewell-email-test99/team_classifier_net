using Microsoft.AspNetCore.Mvc;
using Python.Runtime;

namespace Email_Classifier_Test3.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class TeamController : ControllerBase
    {
        // Static constructor to initialize Python runtime and set Python DLL
        static TeamController()
        {
            // Set the path to the Python DLL
            Runtime.PythonDLL = @"C:\Users\Mukul\AppData\Local\Programs\Python\Python312\python312.dll";

            // Initialize the Python runtime
            PythonEngine.Initialize();
        }

        [HttpGet]
        public ActionResult<string> GetResult(string description)
        {
            using (Py.GIL())
            {
                dynamic script = Py.Import("myScript");

                // Define input_data using the provided description
                string[] input_data = new string[] { description };

                // Call the team_classifier function and pass input_data as an argument
                string result = script.team_classifier(input_data);

                // Return the result
                return Ok(result);
            }
        }
    }
}
