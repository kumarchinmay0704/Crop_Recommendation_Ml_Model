# Contributing to Crop Recommendation System

Thank you for your interest in contributing to the Crop Recommendation System! This document provides guidelines for contributing to this project.

## 🤝 How to Contribute

### Reporting Bugs

1. **Check existing issues** - Search the issues to see if the bug has already been reported
2. **Create a new issue** - Use the bug report template
3. **Provide detailed information**:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

### Suggesting Enhancements

1. **Check existing issues** - Search for similar feature requests
2. **Create a new issue** - Use the feature request template
3. **Describe the enhancement**:
   - Clear description of the feature
   - Use cases and benefits
   - Implementation suggestions (if any)

### Code Contributions

#### Prerequisites

- Python 3.7 or higher
- Git
- Basic knowledge of Flask and machine learning

#### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r crop_app3/requirements.txt
   ```

4. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Making Changes

1. **Follow the coding style**:
   - Use PEP 8 for Python code
   - Add comments for complex logic
   - Use meaningful variable names
   - Keep functions small and focused

2. **Test your changes**:
   ```bash
   python test_app.py
   ```

3. **Update documentation**:
   - Update README.md if needed
   - Add docstrings to new functions
   - Update API documentation if applicable

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   - Use the PR template
   - Describe your changes clearly
   - Link related issues

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows the project's style guidelines
- [ ] Tests pass locally
- [ ] Documentation is updated
- [ ] No new warnings are generated
- [ ] Code is self-documenting with clear variable names

### Pull Request Template

```markdown
## Description
Brief description of the changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Testing
- [ ] Local tests pass
- [ ] Application runs without errors
- [ ] New functionality tested

## Screenshots (if applicable)
Add screenshots for UI changes.

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] I have made corresponding changes to documentation
- [ ] My changes generate no new warnings
```

## 🧪 Testing

### Running Tests

```bash
# Run the test suite
python test_app.py

# Run with verbose output
python -v test_app.py
```

### Writing Tests

When adding new features, include tests:

```python
def test_new_feature():
    """Test the new feature functionality."""
    # Test implementation
    assert expected_result == actual_result
```

## 📚 Documentation

### Code Documentation

- Add docstrings to all functions and classes
- Use clear, descriptive comments
- Follow Google or NumPy docstring style

### API Documentation

- Update `API_DOCUMENTATION.md` for new endpoints
- Include request/response examples
- Document error codes and messages

## 🎯 Areas for Contribution

### High Priority

- [ ] Improve model accuracy
- [ ] Add more crop types
- [ ] Enhance UI/UX
- [ ] Add data validation
- [ ] Implement caching

### Medium Priority

- [ ] Add user authentication
- [ ] Create mobile app
- [ ] Add historical data tracking
- [ ] Implement recommendation explanations
- [ ] Add weather integration

### Low Priority

- [ ] Add multilingual support
- [ ] Create admin dashboard
- [ ] Add export functionality
- [ ] Implement notifications

## 🏷️ Issue Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## 📞 Getting Help

- **GitHub Issues**: For bug reports and feature requests
- **Discussions**: For questions and general discussion
- **Wiki**: For detailed documentation

## 🎉 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to the Crop Recommendation System! 🌾 