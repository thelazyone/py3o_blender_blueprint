use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn hello_blender() -> PyResult<String> {
    Ok("Hello from Rust!".to_string())
}

// Change this function name to match the Python module name expected
#[pymodule]
fn hello_plugin_lib(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_blender, m)?)?;
    Ok(())
}