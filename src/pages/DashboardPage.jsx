import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
  Container, 
  Typography, 
  Box, 
  Grid, 
  Paper, 
  Button,
  Divider,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Avatar
} from '@mui/material';
import { styled } from '@mui/material/styles';
import PersonIcon from '@mui/icons-material/Person';
import CalendarTodayIcon from '@mui/icons-material/CalendarToday';
import Logo from "../assets/images/dark-web/darkweb_logo.png";

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  height: '100%',
  boxShadow: '0px 4px 12px rgba(0, 0, 0, 0.1)',
  borderRadius: '8px',
}));

const DashboardPage = () => {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [searchHistory, setSearchHistory] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('token');
    const userData = localStorage.getItem('user');

    if (!token || !userData) {
      navigate('/login');
      return;
    }

    setUser(JSON.parse(userData));

    // Fetch real-time search history from backend
    const fetchHistory = async () => {
      try {
        const res = await fetch("http://localhost:5050/api/search-history");
        const data = await res.json();
        setSearchHistory(data);
      } catch (err) {
        console.error("Failed to load search history:", err);
      }
    };

    fetchHistory();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    navigate('/login');
  };

  const handleSearchPersonalInfo = () => {
    navigate('/search-personal-info');
  };

  if (!user) return null;

  return (
    <Container maxWidth="lg" sx={{ display: 'flex', justifyContent: 'center' }}>
      <Box sx={{ my: 4, width: '100%' }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 4 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mx: 'auto' }}>
            <img src={Logo} alt="Dark Web Logo" style={{ width: 80, height: 90 }} />
            <Typography component="h1" variant="h4" color="primary" sx={{ fontFamily: 'Times New Roman, serif' }}>
              My Dashboard
            </Typography>
          </Box>

          <Button variant="outlined" onClick={handleLogout} sx={{ fontFamily: 'Times New Roman, serif' }}>
            Logout
          </Button>
        </Box>

        <Grid container spacing={3}>
          <Grid item xs={12} md={6}>
            <StyledPaper sx={{ fontFamily: 'Times New Roman, serif' }}>
              <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mb: 3 }}>
                <Avatar 
                  sx={{ width: 80, height: 80, bgcolor: 'primary.main', mb: 2 }}
                >
                  <PersonIcon fontSize="large" />
                </Avatar>
                <Typography variant="h5" sx={{ fontFamily: 'Times New Roman, serif' }}>
                  {user.firstName || 'John'} {user.lastName || 'Doe'}
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ fontFamily: 'Times New Roman, serif' }}>
                  {user.email || 'user@example.com'}
                </Typography>
              </Box>

              <Divider sx={{ my: 2 }} />

              <List>
                <ListItem>
                  <ListItemIcon><PersonIcon /></ListItemIcon>
                  <ListItemText 
                    primary="Account Details" 
                    secondary="Manage your personal information"
                    primaryTypographyProps={{ sx: { fontFamily: 'Times New Roman, serif' } }}
                    secondaryTypographyProps={{ sx: { fontFamily: 'Times New Roman, serif' } }}
                  />
                </ListItem>
                <ListItem>
                  <ListItemIcon><CalendarTodayIcon /></ListItemIcon>
                  <ListItemText 
                    primary="Activity Logs" 
                    secondary="View your recent activities"
                    primaryTypographyProps={{ sx: { fontFamily: 'Times New Roman, serif' } }}
                    secondaryTypographyProps={{ sx: { fontFamily: 'Times New Roman, serif' } }}
                  />
                </ListItem>
              </List>

              <Box sx={{ mt: 3 }}>
                <Button 
                  variant="contained" 
                  fullWidth 
                  onClick={handleSearchPersonalInfo}
                  sx={{ py: 1.5, fontFamily: 'Times New Roman, serif' }}
                >
                  Search Personal Information
                </Button>
              </Box>
            </StyledPaper>
          </Grid>

          <Grid item xs={12} md={6}>
            <StyledPaper sx={{ fontFamily: 'Times New Roman, serif', height: 300, overflowY: 'auto' }}>
              <Typography variant="h6" sx={{ mb: 2, fontFamily: 'Times New Roman, serif' }}>
                Search History
              </Typography>
              <List>
                {searchHistory.length > 0 ? (
                  searchHistory.map((item, index) => (
                    <ListItem key={index} alignItems="flex-start">
                      <ListItemText
                        primary={`Type: ${item.type} | URL: ${item.url}`}
                        secondary={
                          item.results?.length ? (
                            <Box component="div" sx={{ whiteSpace: 'pre-wrap', fontSize: '0.85rem' }}>
                              {item.results.map((line, i) => <div key={i}>• {line}</div>)}
                            </Box>
                          ) : "No result output."
                        }
                        primaryTypographyProps={{ sx: { fontFamily: 'Times New Roman, serif', fontWeight: 'bold' } }}
                        secondaryTypographyProps={{ sx: { fontFamily: 'Times New Roman, serif' } }}
                      />
                    </ListItem>
                  ))
                ) : (
                  <Typography variant="body2" color="text.secondary" sx={{ fontFamily: 'Times New Roman, serif' }}>
                    No search history yet.
                  </Typography>
                )}
              </List>
            </StyledPaper>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default DashboardPage;

