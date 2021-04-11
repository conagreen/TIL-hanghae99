package com.sparta.springcore.security;

import com.sparta.springcore.model.User;
import org.springframework.security.core.userdetails.UserDetails;

public class UserDetailsImpl implements UserDetails {
    public UserDetailsImpl(User user) {
    }
}
